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
    api = Cov19API(
        filters=brighton_and_hove,
        structure=cases,
    )

    df = api.get_dataframe()

    date = df['date'].to_list()
    daily_cases = df['newCasesBySpecimenDate'].to_list()

    date.reverse()
    daily_cases.reverse()

    options = Options()

    options.ClearSeries()
    options.SetTitle('Brighton and Hove New Daily Cases')
    options.SetxAxisTitle('Date')
    options.SetyAxisTitle('New Cases')
    options.AddSeries('Daily Cases', 'column', daily_cases)
    options.SetCategories(date)

    context = {}
    context['options'] = options.__str__()

    return render(request, 'highcharts/index.html', context)
