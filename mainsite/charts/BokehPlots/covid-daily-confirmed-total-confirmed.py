from datetime import datetime

from bokeh.plotting import figure, curdoc, ColumnDataSource
from bokeh.models import CheckboxGroup, HoverTool
from bokeh.layouts import column, row

from CovidData import CovidData

t1 = datetime.now()

country_data = CovidData()

checkboxes = CheckboxGroup(labels = country_data.menu, sizing_mode='fixed', height=650, width=200)

plot = figure(title         = 'Mean Daily Confirmed against Total Confirmed',
              x_axis_label  = 'Total Confirmed',
              y_axis_label  = 'Mean Daily Confirmed',
              x_axis_type   = 'log',
              y_axis_type   = 'log',
              tools         = 'pan, wheel_zoom, reset',
              active_drag   = 'pan',
              active_scroll = 'wheel_zoom',
              sizing_mode   = 'stretch_both')

# Setup the tooltips
tooltips = [('Country', '$name'),
            ('Confirmed Cases', '@confirmed'),
            ('Mean Daily Confirmed Cases', '@MeanDailyConfirmed'),
            ('Date', '@date{%F}')]

# Add the date formatter
formatters = { '@date' : 'datetime' }

# Create a hover tool
hover_tool = HoverTool()

# Set the tooltips
hover_tool.tooltips = tooltips

# Formatter for dates
hover_tool.formatters = formatters

# Add the tooltip
plot.add_tools(hover_tool)

t2 = datetime.now()
t5 = datetime.now()

for country in country_data:
    country_df = country_data.GetDataFrame(country)
    country_cds = ColumnDataSource(country_df)
    country_data.glyph_dict[country] = plot.line(x = 'confirmed',
                                                 y = 'MeanDailyConfirmed',
                                                 source = country_cds,
                                                 name = country,
                                                 line_color = country_data.colour_dict[country],
                                                 line_width = 1)

    country_data.glyph_dict[country].visible = False

t3 = datetime.now()

print(t2 - t1)
print(t3 - t2)

def SelectCountry(attr, old, new):
    now_selected = list(set(new) - set(old))
    was_selected = list(set(old) - set(new))

    if now_selected:
        country = checkboxes.labels[now_selected[0]]
        country_data.glyph_dict[country].visible = True

    elif was_selected:
        country = checkboxes.labels[was_selected[0]]
        country_data.glyph_dict[country].visible = False

checkboxes.on_change('active', SelectCountry)

Column = column(checkboxes, sizing_mode = 'fixed', height=650, width=200, css_classes=['scrollable'])

Row = row(Column, plot)

Row.sizing_mode = 'stretch_both'

curdoc().add_root(Row)
