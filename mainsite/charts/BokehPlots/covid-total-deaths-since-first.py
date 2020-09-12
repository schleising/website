from libs.multi_line_chart import MultiLineChart

# Setup the tooltips
tooltips = [('Country', '$name'),
            ('Deaths', '@deaths'),
            ('Day Count', '@DayCount')]

MultiLineChart('Total Deaths Since First',
               'Day',
               'Deaths',
               'DayCount',
               'deaths',
               x_axis_type = 'linear',
               y_axis_type = 'log',
               tooltips = tooltips,
               tail = True,
               tail_threshold = 3)
