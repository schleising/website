from libs.multi_line_chart import MultiLineChart

# Setup the tooltips
tooltips = [('Country', '$name'),
            ('Deaths', '@MeanDailyDeaths'),
            ('Day Count', '@DayCount'),
            ('Date', '@date{%F}')]

# Add the date formatter
formatters = { '@date' : 'datetime' }

MultiLineChart('Daily Deaths Since First',
               'Day',
               'Deaths',
               'DayCount',
               'MeanDailyDeaths',
               x_axis_type = 'linear',
               y_axis_type = 'log',
               tooltips = tooltips,
               formatters = formatters,
               tail = True,
               tail_threshold = 3)
