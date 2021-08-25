from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from django.http.response import JsonResponse

from utils.covid_data.global_data import GetGlobalData
from utils.colours.colours import randomColourAsRGBA

import pandas as pd

from .libs.chart_js_dataclass import ChartJS, Dataset

totalDays = 0

# Generate Average Data
def GenerateAverages(country, data_request):
    if country == 'Tim':
        print(totalDays)
        averages = [0 if index < 576 else 1 for index in range(totalDays)]
    else:
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
    countries.insert(0, 'Tim')

    df = pd.DataFrame(json_data[default_country])

    date = df['date'].to_list()

    average_daily_cases = GenerateAverages(default_country, 'AverageDailyCases')

    global totalDays
    totalDays = len(average_daily_cases)

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

def GetDailyCasesAgainstTotalCasesData(country):
    json_data = GetGlobalData()

    df = pd.DataFrame(json_data[country])

    average_daily_cases = GenerateAverages(country, 'AverageDailyCases')
    total_cases = df['confirmed'].to_list()

    data = [{ 'x': x_points, 'y': y_points} for x_points, y_points in zip(total_cases, average_daily_cases)]

    return data

# Create your views here.
def DailyCasesAgainstTotalCases(request):
    default_country = 'United Kingdom'

    json_data = GetGlobalData()

    countries = [country for country in json_data]

    data = GetDailyCasesAgainstTotalCasesData(default_country)

    chart = ChartJS()

    chart.SetLabel('Daily Cases against Total Cases')
    chart.SetxAxis('logarithmic')
    chart.SetyAxis('logarithmic')

    chart.AddDataset(default_country, data, 'scatter', randomColourAsRGBA(default_country))

    context = {}
    context['chart'] = chart.chartjs_dict
    context['countries'] = countries

    return render(request, 'chartjs/daily_cases_total_cases.html', context)

def CheckboxClicked(request : WSGIRequest):
    country = request.GET.get('country')
    data_request = request.GET.get('DataRequest')

    print(country)
    print(data_request)

    if data_request == 'DailyCasesTotalCases':
        data = GetDailyCasesAgainstTotalCasesData(country)
    else:
        data = GenerateAverages(country, data_request)

    dataset = Dataset()
    dataset.AddDataset(f'{country}', data, 'line', randomColourAsRGBA(country))

    return JsonResponse(dataset.dataset_dict)
