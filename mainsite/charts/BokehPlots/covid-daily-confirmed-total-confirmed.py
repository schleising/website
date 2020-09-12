from libs.multi_line_chart import MultiLineChart

MultiLineChart('Mean Daily Confirmed against Total Confirmed',
               'Total Confirmed',
               'Mean Daily Confirmed',
               'confirmed',
               'MeanDailyConfirmed',
               x_axis_type = 'log',
               y_axis_type = 'log')
