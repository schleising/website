from libs.multi_line_chart import MultiLineChart

# Setup the tooltips
tooltips = [('Country', '$name'),
            ('Deaths', '@deaths'),
            ('Date', '@date{%F}')]

# Add the date formatter
formatters = { '@date' : 'datetime' }

MultiLineChart('Deaths against Time',
               'Date',
               'Deaths',
               'date',
               'deaths',
               x_axis_type = 'datetime',
               y_axis_type = 'log',
               tooltips = tooltips,
               formatters = formatters)
