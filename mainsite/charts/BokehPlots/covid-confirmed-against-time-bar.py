from libs.bar_chart import BarChart

# Setup the tooltips
tooltips = [('Country', '$name'),
            ('Confirmed', '@DailyConfirmed'),
            ('Date', '@date{%F}')]

# Add the date formatter
formatters = { '@date' : 'datetime' }

BarChart('Confirmed against Time (Bar)',
         'Date',
         'Confirmed',
         'date',
         'DailyConfirmed',
         x_axis_type = 'datetime',
         y_axis_type = 'linear',
         tooltips = tooltips,
         formatters = formatters)
