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

def daily_confirmed_total_confirmed(request):
    bokeh_server_url = "%sbokehproxy/covid-daily-confirmed-total-confirmed" % (request.build_absolute_uri(location='/'))
    server_script = server_session(None, session_id=session_id.generate_session_id(), url=bokeh_server_url)
    context = {"server_script": server_script,
               }
    return render(request, 'charts/daily-confirmed-total-confirmed.html', context)

def daily_confirmed_vs_time(request):
    bokeh_server_url = "%sbokehproxy/covid-daily-confirmed-cases" % (request.build_absolute_uri(location='/'))
    server_script = server_session(None, session_id=session_id.generate_session_id(), url=bokeh_server_url)
    context = {"server_script": server_script,
               }
    return render(request, 'charts/daily-confirmed-cases.html', context)

def active_cases_vs_time(request):
    bokeh_server_url = "%sbokehproxy/covid-active-against-time" % (request.build_absolute_uri(location='/'))
    server_script = server_session(None, session_id=session_id.generate_session_id(), url=bokeh_server_url)
    context = {"server_script": server_script,
               }
    return render(request, 'charts/active-cases.html', context)

def deaths_vs_time(request):
    bokeh_server_url = "%sbokehproxy/covid-deaths-against-time" % (request.build_absolute_uri(location='/'))
    server_script = server_session(None, session_id=session_id.generate_session_id(), url=bokeh_server_url)
    context = {"server_script": server_script,
               }
    return render(request, 'charts/deaths-against-time.html', context)

def total_deaths_since_first(request):
    bokeh_server_url = "%sbokehproxy/covid-total-deaths-since-first" % (request.build_absolute_uri(location='/'))
    server_script = server_session(None, session_id=session_id.generate_session_id(), url=bokeh_server_url)
    context = {"server_script": server_script,
               }
    return render(request, 'charts/total-deaths-since-first.html', context)

def daily_deaths_since_first(request):
    bokeh_server_url = "%sbokehproxy/covid-daily-deaths-since-first" % (request.build_absolute_uri(location='/'))
    server_script = server_session(None, session_id=session_id.generate_session_id(), url=bokeh_server_url)
    context = {"server_script": server_script,
               }
    return render(request, 'charts/daily-deaths-since-first.html', context)

def country_stats(request):
    bokeh_server_url = "%sbokehproxy/covid-country-stats" % (request.build_absolute_uri(location='/'))
    server_script = server_session(None, session_id=session_id.generate_session_id(), url=bokeh_server_url)
    context = {"server_script": server_script,
               }
    return render(request, 'charts/country-stats.html', context)

def deaths_against_time_bar(request):
    bokeh_server_url = "%sbokehproxy/covid-deaths-against-time-bar" % (request.build_absolute_uri(location='/'))
    server_script = server_session(None, session_id=session_id.generate_session_id(), url=bokeh_server_url)
    context = {"server_script": server_script,
               }
    return render(request, 'charts/deaths-against-time-bar.html', context)
