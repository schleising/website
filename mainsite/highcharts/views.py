from django.shortcuts import render
from uk_covid19 import Cov19API

from .libs.options_dataclass import Options

brighton_and_hove = [
    "areaType=utla",
    "areaName=Brighton and Hove",
]

cases = {
    "date": "date",
    "areaName": "areaName",
    "newCasesBySpecimenDate": "newCasesBySpecimenDate",
    "cumCasesBySpecimenDate": "cumCasesBySpecimenDate",
    "cumCasesBySpecimenDateRate": "cumCasesBySpecimenDateRate",
}

# Create your views here.
def index(request):
    return NewCasesBarChart(request)

def NewCasesBarChart(request):
    api = Cov19API(
        filters=brighton_and_hove,
        structure=cases,
    )

    df = api.get_dataframe()

    df = df[::-1]

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

    return render(request, 'highcharts/new_cases_bar_chart.html', context)
