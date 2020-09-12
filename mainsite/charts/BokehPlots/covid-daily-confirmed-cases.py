from libs.multi_line_chart import MultiLineChart

# Setup the tooltips
tooltips = [('Country', '$name'),
            ('Mean Daily Confirmed Cases', '@MeanDailyConfirmed'),
            ('Date', '@date{%F}')]

# Add the date formatter
formatters = { '@date' : 'datetime' }

MultiLineChart('Daily Confirmed Cases',
               'Date',
               'Mean Daily Confirmed',
               'date',
               'MeanDailyConfirmed',
               x_axis_type = 'datetime',
               y_axis_type = 'log',
               tooltips = tooltips,
               formatters = formatters)
