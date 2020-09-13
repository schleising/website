from libs.bar_chart import BarChart

# Setup the tooltips
tooltips = [('Country', '$name'),
            ('Deaths', '@DailyDeaths'),
            ('Date', '@date{%F}')]

# Add the date formatter
formatters = { '@date' : 'datetime' }

BarChart('Deaths against Time (Bar)',
         'Date',
         'Deaths',
         'date',
         'DailyDeaths',
         x_axis_type = 'datetime',
         y_axis_type = 'linear',
         tooltips = tooltips,
         formatters = formatters)
