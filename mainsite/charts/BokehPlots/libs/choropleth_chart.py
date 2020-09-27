from bokeh.plotting import figure, curdoc
from bokeh.models import HoverTool, LogColorMapper, ColorBar, GeoJSONDataSource, NumeralTickFormatter, LogTicker
from bokeh.tile_providers import CARTODBPOSITRON, get_provider
from bokeh.palettes import brewer

import pandas as pd
from pandas.io.parsers import count_empty_vals

class ChoroplethChart:
    def __init__(self, title, tooltips, column, colour, line_colour, country_data = None):
        self.title = title
        self.column = column
        self.tooltips = tooltips
        self.colour = colour
        self.line_colour = line_colour

        if type(country_data).__name__ == 'NoneType':
            self.country_data = pd.read_pickle('geodata/geodata.pickle')
        else:
            self.country_data = country_data

        self.ConfirmedMapPlot()

    def AddToolTip(self, plot, tooltips, formatters = None):
        # Create a hover tool
        hover_tool = HoverTool()

        # Set the tooltips
        hover_tool.tooltips = tooltips

        # Formatter for dates
        hover_tool.formatters = formatters

        # Add the tooltip
        plot.add_tools(hover_tool)

        return hover_tool

    # Create a map plot of latest confirmed cases
    def ConfirmedMapPlot(self):
        # Get the tile provider
        tile_provider = get_provider(CARTODBPOSITRON)

        # Create the plot
        plot = figure(x_axis_type="mercator", 
                      y_axis_type="mercator",
                      title=self.title, 
                      tools = 'pan, wheel_zoom, reset',
                      active_drag   = 'pan',
                      active_scroll = 'wheel_zoom')

        # Add the tile streamer to the plot
        plot.add_tile(tile_provider)

        # Set the sizing mode
        plot.sizing_mode = 'stretch_both'

        # Transform from WGS83 to Web Mercator projection
        merc_geo_json_df = self.country_data.to_crs('EPSG:3857')

        # Add the transformed data to a GeoJSONDataSource
        geosource = GeoJSONDataSource(geojson = merc_geo_json_df.to_json())

        # Set the palette and min/max range for the colour mapper
        palette = brewer[self.colour][8]
        palette = palette[::-1]
        min_range = self.country_data[self.column].min()
        max_range = self.country_data[self.column].max()

        # Create the colour mapper
        color_mapper = LogColorMapper(palette = palette, low = min_range, high = max_range)

        # Create a tick formatter
        format_tick = NumeralTickFormatter(format='0.0a')

        # Create a Log Ticker
        log_ticker = LogTicker()

        # Create the colour bar which will go on the right
        color_bar = ColorBar(color_mapper=color_mapper,
                             label_standoff=18,
                             formatter=format_tick,
                             border_line_color=None,
                             location = (0, 0),
                             ticker=log_ticker)

        # Add the data to the circle plot
        plot.patches(xs='xs', 
                     ys='ys', 
                     source=geosource, 
                     line_color=self.line_colour,
                     fill_alpha=0.8, 
                     fill_color={'field' : self.column, 'transform' : color_mapper})

        # Add the colour bar
        plot.add_layout(color_bar, 'right')

        # Add the tooltip
        self.AddToolTip(plot, self.tooltips)

        curdoc().add_root(plot)
