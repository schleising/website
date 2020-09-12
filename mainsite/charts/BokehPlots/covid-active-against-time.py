from libs.multi_line_chart import MultiLineChart

# Setup the tooltips
tooltips = [('Country', '$name'),
            ('Active Cases', '@ActiveCases'),
            ('Date', '@date{%F}')]

# Add the date formatter
formatters = { '@date' : 'datetime' }

MultiLineChart('Active Cases against Time',
               'Date',
               'Active Cases',
               'date',
               'ActiveCases',
               x_axis_type = 'datetime',
               y_axis_type = 'log',
               tooltips = tooltips,
               formatters = formatters)
