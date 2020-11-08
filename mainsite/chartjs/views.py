from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from django.http.response import JsonResponse

from utils.covid_data.global_data import GetGlobalData
from utils.colours.colours import randomColourAsRGBA

import pandas as pd

from .libs.chart_js_dataclass import ChartJS, Dataset

# Create your views here.
def NewCasesAgainstTime(request):
    json_data = GetGlobalData()

    countries = [country for country in json_data]

    df = pd.DataFrame(json_data['United Kingdom'])

    df['daily_confirmed'] = df['confirmed'].diff()

    # Use DataFrame.rolling() to generate running average data
    rolling = df.rolling(7)

    # Calculate the rolling mean of the whole data frame
    mean = rolling.mean()

    # Add the rolling mean columns to the data frame
    df['MeanDailyConfirmed'] = mean['daily_confirmed'].round()

    df.fillna(0, inplace=True)

    date = df['date'].to_list()
    # daily_cases = df['daily_confirmed'].to_list()
    average_daily_cases = df['MeanDailyConfirmed'].to_list()

    chart = ChartJS()

    chart.SetLabel('Daily Confirmed Cases')
    chart.SetCategories(date)
    chart.SetyAxis('logarithmic')

    chart.AddDataset('United Kingdom', average_daily_cases, 'line', randomColourAsRGBA('United Kingdom'))

    context = {}
    context['chart'] = chart.chartjs_dict
    context['countries'] = countries

    return render(request, 'chartjs/global_new_cases.html', context)

def CheckboxClicked(request : WSGIRequest):
    country = request.GET.get('country')

    json_data = GetGlobalData()

    df = pd.DataFrame(json_data[country])

    df['daily_confirmed'] = df['confirmed'].diff()

    # Use DataFrame.rolling() to generate running average data
    rolling = df.rolling(7)

    # Calculate the rolling mean of the whole data frame
    mean = rolling.mean()

    # Add the rolling mean columns to the data frame
    df['MeanDailyConfirmed'] = mean['daily_confirmed'].round()

    df.fillna(0, inplace=True)

    average_daily_cases = df['MeanDailyConfirmed'].to_list()

    dataset = Dataset()
    dataset.AddDataset(f'{country}', average_daily_cases, 'line', randomColourAsRGBA(country))

    return JsonResponse(dataset.dataset_dict)
