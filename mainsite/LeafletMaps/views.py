from django.shortcuts import render

import json
import geopandas
import numpy as np
import pandas as pd

from uk_covid19 import Cov19API

all_nations = [
    "areaType=utla",
]

cases_and_deaths = {
    "date": "date",
    "areaName": "areaName",
    "areaCode": "areaCode",
    "newCasesByPublishDate": "newCasesByPublishDate",
    "cumCasesByPublishDate": "cumCasesByPublishDate",
    "newDeathsByDeathDate": "newDeathsByDeathDate",
    "cumDeathsByDeathDate": "cumDeathsByDeathDate"
}

# Create your views here.
def index(request):
    return uk_cumulative_cases(request)

def uk_cumulative_cases(request):

    api = Cov19API(
        filters=all_nations,
        structure=cases_and_deaths,
        latest_by="newCasesByPublishDate"
    )

    df = api.get_dataframe()

    pop_df = pd.read_csv('LeafletMaps/data/uk_population.csv')

    pop_merged_df = df.merge(pop_df, left_on='areaCode', right_on='Code')

    geo_df = geopandas.read_file('LeafletMaps/data/Counties_and_Unitary_Authorities__December_2019__Boundaries_UK_BUC.geojson')

    geo_merged_df = geopandas.GeoDataFrame(pop_merged_df.merge(geo_df, left_on='areaCode', right_on='ctyua19cd'))

    # Set the coordinate reference system EPSG:4326 (WGS84 Lat/Long)
    geo_merged_df.crs = 'epsg:4326'

    # Tell GeoPandas that the column named geometry contains the points describing the countries
    geo_merged_df.set_geometry('geometry')

    geo_merged_df['ConfPerCap'] = (geo_merged_df['cumCasesByPublishDate'] / geo_merged_df['Population']) * 10000

    min_cpc = np.math.log(min(geo_merged_df['ConfPerCap']))
    max_cpc = np.math.log(max(geo_merged_df['ConfPerCap']))

    graduations_ndarray = np.linspace(min_cpc, max_cpc, 7)
    graduations = [np.math.exp(x) for x in graduations_ndarray]

    context = {}
    context['geo_data'] = json.loads(geo_merged_df.to_json())
    context['graduations'] = graduations

    return render(request, 'LeafletMaps/uk_cumulative_cases.html', context=context)
