from libs.choropleth_chart import ChoroplethChart

# Setup the tooltips
tooltips = [('Country', '@Country'),
            ('Confirmed per Capita', '@ConfPerCap')]

choropleth = ChoroplethChart('Confirmed PC Map Plot', tooltips, 'ConfPerCap', 'Blues', 'blue')
