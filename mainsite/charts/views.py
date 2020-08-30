from django.shortcuts import render
from bokeh.plotting import figure, output_file, show
from bokeh.embed import components, server_session
from bokeh.util import session_id

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

def Test(request):
    bokeh_server_url = "%sbokehproxy/Test" % (request.build_absolute_uri(location='/'))
    server_script = server_session(None, session_id=session_id.generate_session_id(), url=bokeh_server_url)
    context = {"graphname": "Test",
               "server_script": server_script,
               }
    return render(request, 'charts/Test.html', context)