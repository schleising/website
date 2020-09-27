from libs.choropleth_chart import ChoroplethChart

# Setup the tooltips
tooltips = [('Country', '@Country'),
            ('Confirmed', '@Confirmed')]

choropleth = ChoroplethChart('Confirmed Map Plot', tooltips, 'Confirmed', 'Reds', 'red')
