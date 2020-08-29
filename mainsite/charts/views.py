from django.shortcuts import render
from bokeh.plotting import figure, output_file, show
from bokeh.embed import components

import numpy as np

# Create your views here.
def CreateChart(request):
    x = np.arange(-10, 11)
    y = x * x

    plot = figure(title = 'Graph Test', x_axis_label = 'x', y_axis_label = 'y', sizing_mode = 'stretch_both')

    plot.line(x=x, y=y, line_width = 2)

    script, div = components(plot)

    context = { 'script' : script, 'div' : div }

    return render(request, 'charts/index.html', context)
