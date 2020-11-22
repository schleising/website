from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from django.http.response import JsonResponse
from numpy.lib.function_base import _average_dispatcher

from utils.covid_data.global_data import GetGlobalData
from utils.colours.colours import randomColourAsRGBA

import pandas as pd

from .libs.chart_js_dataclass import ChartJS, Dataset

# Generate Average Data
def GenerateAverages(country, data_request):
    json_data = GetGlobalData()

    df = pd.DataFrame(json_data[country])

    df['daily_confirmed'] = df['confirmed'].diff()
    df['daily_deaths']    = df['deaths'].diff()

    # Use DataFrame.rolling() to generate running average data
    rolling = df.rolling(7)

    # Calculate the rolling mean of the whole data frame
    mean = rolling.mean()

    # Add the rolling mean columns to the data frame
    df['AverageDailyCases']  = mean['daily_confirmed'].round()
    df['AverageDailyDeaths'] = mean['daily_deaths'].round()

    df.fillna(0, inplace=True)

    averages = df[data_request].to_list()

    return averages

# Create your views here.
def NewCasesAgainstTime(request):
    default_country = 'United Kingdom'

    json_data = GetGlobalData()

    countries = [country for country in json_data]

    df = pd.DataFrame(json_data[default_country])

    date = df['date'].to_list()

    average_daily_cases = GenerateAverages(default_country, 'AverageDailyCases')

    chart = ChartJS()

    chart.SetLabel('Daily Confirmed Cases')
    chart.SetCategories(date)
    chart.SetyAxis('logarithmic')

    chart.AddDataset(default_country, average_daily_cases, 'line', randomColourAsRGBA(default_country))

    context = {}
    context['chart'] = chart.chartjs_dict
    context['countries'] = countries

    return render(request, 'chartjs/global_new_cases.html', context)

# Create your views here.
def DeathsAgainstTime(request):
    default_country = 'United Kingdom'

    json_data = GetGlobalData()

    countries = [country for country in json_data]

    df = pd.DataFrame(json_data[default_country])

    date = df['date'].to_list()

    average_daily_cases = GenerateAverages(default_country, 'AverageDailyDeaths')

    chart = ChartJS()

    chart.SetLabel('Daily Deaths')
    chart.SetCategories(date)
    chart.SetyAxis('logarithmic')

    chart.AddDataset(default_country, average_daily_cases, 'line', randomColourAsRGBA(default_country))

    context = {}
    context['chart'] = chart.chartjs_dict
    context['countries'] = countries

    return render(request, 'chartjs/global_deaths.html', context)

def CheckboxClicked(request : WSGIRequest):
    country = request.GET.get('country')
    data_request = request.GET.get('DataRequest')

    # For future reference, this is a function call !!
    data = GenerateAverages(country, data_request)

    dataset = Dataset()
    dataset.AddDataset(f'{country}', data, 'line', randomColourAsRGBA(country))

    return JsonResponse(dataset.dataset_dict)
