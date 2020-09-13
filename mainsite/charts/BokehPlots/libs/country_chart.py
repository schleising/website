from bokeh.plotting import figure, curdoc, ColumnDataSource
from bokeh.models import RadioGroup, HoverTool
from bokeh.layouts import column, row

import numpy as np

from .CovidData import CovidData

# Creates a plot of deaths against time
class CountryChart:
    def AddToolTip(self, plot, tooltips, formatters):
        # Create a hover tool
        hover_tool = HoverTool()

        # Set the tooltips
        hover_tool.tooltips = tooltips

        # Formatter for dates
        hover_tool.formatters = formatters

        # Add the tooltip
        plot.add_tools(hover_tool)

        return hover_tool

    def __init__(self,
                 x_axis_label,
                 y_axis_label,
                 x_axis_type = 'linear',
                 y_axis_type = 'linear'):

        # Set the x and y data here so it only needs to be changed in one place
        x_data = 'date'

        rg_height = 595
        rg_width  = 160

        country_data = CovidData()

        radiogroup = RadioGroup(labels = country_data.menu,
                                active = country_data.menu.index('United Kingdom'),
                                sizing_mode = 'fixed', height = rg_height, width = rg_width)

        # Create the figure
        plot = figure(x_axis_label  = x_axis_label,
                      y_axis_label  = y_axis_label,
                      x_axis_type   = x_axis_type,
                      y_axis_type   = y_axis_type,
                      tools         = 'pan, wheel_zoom, reset',
                      active_drag   = 'pan',
                      active_scroll = 'wheel_zoom',
                      sizing_mode   = 'stretch_both')

        def UpdateChart(country):

            plot.title.text = '{0} Stats'.format(country)

            self.column_data = ColumnDataSource(country_data.GetDataFrame(country))
            deaths_line = plot.line(x=x_data,
                                    y='deaths',
                                    source=self.column_data,
                                    legend_label='Deaths',
                                    line_color='red')

            confirmed_line = plot.line(x=x_data,
                                    y='confirmed',
                                    source=self.column_data,
                                    legend_label='Confirmed Cases',
                                    line_color='blue')

            recovered_line = plot.line(x=x_data,
                                    y='recovered',
                                    source=self.column_data,
                                    legend_label='Recoveries',
                                    line_color='green')

            active_line = plot.line(x=x_data,
                                    y='ActiveCases',
                                    source=self.column_data,
                                    legend_label='Active Cases',
                                    line_color='mediumaquamarine')

            # self.deaths_ds    = deaths_line.data_source
            # self.confirmed_ds = confirmed_line.data_source
            # self.recovered_ds = recovered_line.data_source
            # self.active_ds    = active_line.data_source

            # Set the legend location to top left, out of the way
            plot.legend.location='top_left'

            # Allow the data series to be turned on and off by clicking the legend
            plot.legend.click_policy='hide'

            # Set legend transparency
            plot.legend.background_fill_alpha = 0.75

            formatters = { '@date' : 'datetime' }

            # Setup the tooltips
            tooltips = [('Deaths', '@deaths'),
                        ('Date', '@date{%F}')]

            # Add the tooltip
            hover_tool_deaths = self.AddToolTip(plot, tooltips, formatters)

            # Setup the tooltips
            tooltips = [('Confirmed', '@confirmed'),
                        ('Date', '@date{%F}')]

            # Add the tooltip
            hover_tool_confirmed = self.AddToolTip(plot, tooltips, formatters)

            # Setup the tooltips
            tooltips = [('Recovered', '@recovered'),
                        ('Date', '@date{%F}')]

            # Add the tooltip
            hover_tool_recovered = self.AddToolTip(plot, tooltips, formatters)

            # Setup the tooltips
            tooltips = [('Active Cases', '@ActiveCases'),
                        ('Date', '@date{%F}')]

            # Add the tooltip
            hover_tool_active = self.AddToolTip(plot, tooltips, formatters)

            # Ensure the hover tool only renders on the circles
            hover_tool_deaths.renderers    = [deaths_line]
            hover_tool_confirmed.renderers = [confirmed_line]
            hover_tool_recovered.renderers = [recovered_line]
            hover_tool_active.renderers    = [active_line]

        def callback(active):
            country = radiogroup.labels[active]
            country_cds = ColumnDataSource(country_data.GetDataFrame(country))

            self.column_data.data = dict(country_cds.data)

            plot.title.text = '{0} Stats'.format(country)

        radiogroup.on_click(callback)

        UpdateChart('United Kingdom')

        Column = column(radiogroup, sizing_mode = 'fixed', height = rg_height, width = rg_width, css_classes=['scrollable'])

        Row = row(Column, plot)

        Row.sizing_mode = 'stretch_both'

        curdoc().add_root(Row)
