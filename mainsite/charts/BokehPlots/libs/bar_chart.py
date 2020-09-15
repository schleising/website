import copy
from datetime import timedelta
from bokeh.plotting import figure, curdoc, ColumnDataSource
from bokeh.models import CheckboxGroup, HoverTool
from bokeh.layouts import column, row

from .CovidData import CovidData

class BarChart:
    def __init__(self,
                 chart_title,
                 x_axis_label,
                 y_axis_label,
                 x_data,
                 y_data,
                 x_axis_type = 'datetime',
                 y_axis_type = 'linear',
                 tooltips = None,
                 formatters = None,
                 tail = False,
                 tail_threshold = 0):

        cb_height = 595
        cb_width  = 160

        # The country we're looking at
        default_countries = ['France',
                             'United Kingdom',
                             'China',
                             'US',
                             'Brazil',
                             'Australia',
                             'India',
                             'Sweden',
                             'Germany',
                             'Russia',
                             'Philippines',
                             'Nigeria',
                             'Saudi Arabia',
                             'South Africa',
                             'Mexico',
                             'Spain']

        country_data = CovidData()

        checkboxes = CheckboxGroup(labels = country_data.menu, sizing_mode = 'fixed', height = cb_height, width = cb_width)

        plot = figure(title         = chart_title,
                      x_axis_label  = x_axis_label,
                      y_axis_label  = y_axis_label,
                      x_axis_type   = x_axis_type,
                      y_axis_type   = y_axis_type,
                      tools         = 'pan, wheel_zoom, reset',
                      active_drag   = 'pan',
                      active_scroll = 'wheel_zoom',
                      sizing_mode   = 'stretch_both')

        # Return a modified copy of a data frame with dates shifted to bars don't stack
        def BarShiftDates(country_df, country_number, number_of_countries):
            # Make a copy of the data for modification
            new_df = copy.deepcopy(country_df)

            # Shift the dates by the proportion of a day
            new_df['date'] += timedelta(days=((country_number + 0.5) / number_of_countries))

            # Return the new data frame
            return new_df

        def AddDefaultCountries():
            country_number = 0

            for country in sorted(default_countries):
                index = checkboxes.labels.index(country)
                checkboxes.active.append(index)

            # # Set the legend location to top left, out of the way
            # plot.legend.location='top_left'

            # # Allow the data series to be turned on and off by clicking the legend
            # plot.legend.click_policy='hide'

            # # Set legend transparency
            # plot.legend.background_fill_alpha = 0.75

        def SelectCountry(attr, old, new):
            now_selected = list(set(new) - set(old))
            was_selected = list(set(old) - set(new))

            country_number = 0

            if now_selected:
                country = checkboxes.labels[now_selected[0]]

                if country_data.glyph_dict[country] == None:
                    # Shift the dates by the proportion of a day, minus one as world not included
                    shifted_df = BarShiftDates(country_data.GetDataFrame(country), country_number, len(new))
                    # Add this new data frame to a column data source
                    tailed_df = shifted_df.tail(14)
                    column_data = ColumnDataSource(tailed_df)

                    # Plot a bar chart of daily deaths
                    country_data.glyph_dict[country] = plot.vbar(x=x_data,
                                                                bottom=0, 
                                                                top=y_data,
                                                                source=column_data, 
                                                                color=country_data.colour_dict[country], 
                                                                name=country,
                                                                width=timedelta(days=1/(len(new))))

                country_data.glyph_dict[country].visible = True

            elif was_selected:
                country = checkboxes.labels[was_selected[0]]
                country_data.glyph_dict[country].visible = False

            for selection in sorted(new):
                country = checkboxes.labels[selection]

                # Shift the dates by the proportion of a day, minus one as world not included
                shifted_df = BarShiftDates(country_data.GetDataFrame(country), country_number, len(new))
                # Add this new data frame to a column data source
                tailed_df = shifted_df.tail(14)
                column_data = ColumnDataSource(tailed_df)
                country_data.glyph_dict[country].glyph.width = timedelta(days=1/(len(new)))
                country_data.glyph_dict[country].data_source.data = dict(column_data.data)

                country_number += 1

            for tool in plot.tools:
                if type(tool).__name__ == 'HoverTool':
                    plot.tools.remove(tool)

            # Create a hover tool
            hover_tool = HoverTool()

            # Set the tooltips
            hover_tool.tooltips = tooltips

            # Formatter for dates
            hover_tool.formatters = formatters

            # Add the tooltip
            plot.add_tools(hover_tool)

        checkboxes.on_change('active', SelectCountry)

        Column = column(checkboxes, sizing_mode = 'fixed', height = cb_height, width = cb_width, css_classes=['scrollable'])

        Row = row(Column, plot)

        Row.sizing_mode = 'stretch_both'

        AddDefaultCountries()

        curdoc().add_root(Row)
