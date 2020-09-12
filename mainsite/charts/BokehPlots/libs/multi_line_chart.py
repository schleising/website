import copy

from bokeh.plotting import figure, curdoc, ColumnDataSource
from bokeh.models import CheckboxGroup, HoverTool
from bokeh.layouts import column, row

import numpy as np

from .CovidData import CovidData

class MultiLineChart:
    # Return the tail of a frame once the values in the requested column have got above a certain level
    def GetTail(self, country_df_dict, index_label, column, threshold = 0):
        # Get the first index where the data is above the threshold
        first_index = np.argmax(country_df_dict[column] > threshold)

        # Only tail if it's necessary, create a deep copy as we're adding a new column for the day count
        if first_index > 0:
            tailed_df = copy.deepcopy(country_df_dict.tail(-first_index))
        else:
            tailed_df = copy.deepcopy(country_df_dict)

        # Insert the Day Count column
        tailed_df[index_label] = np.arange(len(tailed_df))
        
        # Return the new Data Frame
        return tailed_df

    def __init__(self,
                 chart_title,
                 x_axis_label,
                 y_axis_label,
                 x_data,
                 y_data,
                 x_axis_type = 'linear',
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

        def AddDefaultCountries():
            for country in default_countries:
                index = checkboxes.labels.index(country)
                SelectCountry(None, [], [index])
                checkboxes.active.append(index)

        def SelectCountry(attr, old, new):
            now_selected = list(set(new) - set(old))
            was_selected = list(set(old) - set(new))

            if now_selected:
                country = checkboxes.labels[now_selected[0]]

                if country_data.glyph_dict[country] == None:
                    country_df = country_data.GetDataFrame(country)

                    if tail == True:
                        country_df = self.GetTail(country_df, x_data, y_data, tail_threshold)

                    country_cds = ColumnDataSource(country_df)
                    country_data.glyph_dict[country] = plot.line(x = x_data,
                                                                 y = y_data,
                                                                 source = country_cds,
                                                                 name = country,
                                                                 line_color = country_data.colour_dict[country],
                                                                 line_width = 1)

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

                country_data.glyph_dict[country].visible = True

            elif was_selected:
                country = checkboxes.labels[was_selected[0]]
                country_data.glyph_dict[country].visible = False

        checkboxes.on_change('active', SelectCountry)

        Column = column(checkboxes, sizing_mode = 'fixed', height = cb_height, width = cb_width, css_classes=['scrollable'])

        Row = row(Column, plot)

        Row.sizing_mode = 'stretch_both'

        AddDefaultCountries()

        curdoc().add_root(Row)
