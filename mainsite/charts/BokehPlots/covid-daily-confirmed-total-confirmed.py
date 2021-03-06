from libs.multi_line_chart import MultiLineChart

# Setup the tooltips
tooltips = [('Country', '$name'),
            ('Confirmed Cases', '@confirmed'),
            ('Mean Daily Confirmed Cases', '@MeanDailyConfirmed'),
            ('Date', '@date{%F}')]

# Add the date formatter
formatters = { '@date' : 'datetime' }

MultiLineChart('Mean Daily Confirmed against Total Confirmed',
               'Total Confirmed',
               'Mean Daily Confirmed',
               'confirmed',
               'MeanDailyConfirmed',
               x_axis_type = 'log',
               y_axis_type = 'log',
               tooltips = tooltips,
               formatters = formatters)
