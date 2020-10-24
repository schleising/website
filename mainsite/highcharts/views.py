import json
from django.core.handlers.wsgi import WSGIRequest
from django.http.response import JsonResponse
from django.shortcuts import render

from utils.covid_data.uk_data import GetUKData
from utils.covid_data.global_data import GetGlobalData

import pandas as pd

from .libs.options_dataclass import Options, Series

# Create your views here.
def index(request):
    return NewCasesBarChart(request)

def NewCasesBarChart(request):

    df = GetUKData('Brighton and Hove')

    # Use DataFrame.rolling() to generate running average data
    rolling = df.rolling(7)

    # Calculate the rolling mean of the whole data frame
    mean = rolling.mean()

    # Add the rolling mean columns to the data frame
    df['MeanDailyConfirmed'] = mean['newCasesBySpecimenDate'].round()

    df.fillna(0, inplace=True)

    date = df['date'].to_list()
    daily_cases = df['newCasesBySpecimenDate'].to_list()
    average_daily_cases = df['MeanDailyConfirmed'].to_list()

    options = Options()

    options.SetTitle('Brighton and Hove New Daily Cases')
    options.SetxAxisTitle('Date')
    options.SetyAxisTitle('New Cases')
    options.AddSeries('Daily Cases', 'column', daily_cases)
    options.AddSeries('7 Day Average Daily Cases', 'line', average_daily_cases)
    options.SetCategories(date)

    context = {}
    context['options'] = options.options_dict

    return render(request, 'highcharts/brighton_new_cases_bar_chart.html', context)

def NewCasesAgainstTime(request):
    json_data = GetGlobalData()

    countries = [country for country in json_data]

    df = pd.DataFrame(json_data['United Kingdom'])

    df['daily_confirmed']    = df['confirmed'].diff()
    # df['daily_confirmed'][0] = df['confirmed'][0]

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

    options = Options()

    options.SetTitle('United Kingdom New Daily Cases')
    options.SetxAxisTitle('Date')
    options.SetyAxisTitle('New Cases')
    options.SetyAxisType('logarithmic')
    options.AddSeries('United Kingdom', 'line', average_daily_cases)
    options.SetCategories(date)

    context = {}
    context['options'] = options.options_dict
    context['countries'] = countries

    return render(request, 'highcharts/global_new_cases.html', context)

def CheckboxClicked(request : WSGIRequest):
    checkbox_dict = json.loads(request.body)

    json_data = GetGlobalData()

    df = pd.DataFrame(json_data[checkbox_dict['name']])

    df['daily_confirmed'] = df['confirmed'].diff()

    # Use DataFrame.rolling() to generate running average data
    rolling = df.rolling(7)

    # Calculate the rolling mean of the whole data frame
    mean = rolling.mean()

    # Add the rolling mean columns to the data frame
    df['MeanDailyConfirmed'] = mean['daily_confirmed'].round()

    df.fillna(0, inplace=True)

    average_daily_cases = df['MeanDailyConfirmed'].to_list()

    series = Series()
    series.series_dict['name'] = f"{checkbox_dict['name']}"
    series.series_dict['type'] = 'line'
    series.series_dict['data'] = average_daily_cases

    return JsonResponse(series.series_dict)
