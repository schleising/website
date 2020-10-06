from django.shortcuts import render

import json
import geopandas

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
    return render(request, 'LeafletMaps/index.html')

def uk_cumulative_cases(request):

    api = Cov19API(
        filters=all_nations,
        structure=cases_and_deaths,
        latest_by="newCasesByPublishDate"
    )

    df = api.get_dataframe()

    geo_df = geopandas.read_file('LeafletMaps/data/Counties_and_Unitary_Authorities__December_2019__Boundaries_UK_BUC.geojson')

    merged_df = geopandas.GeoDataFrame(df.merge(geo_df, right_on='ctyua19cd', left_on='areaCode'))

    # Set the coordinate reference system EPSG:4326 (WGS84 Lat/Long)
    merged_df.crs = 'epsg:4326'

    # Tell GeoPandas that the column named geometry contains the points describing the countries
    merged_df.set_geometry('geometry')

    geo_data = merged_df.to_file('uk_covid_data.geojson', driver='GeoJSON')
    with open('uk_covid_data.geojson') as json_file:
        geo_data = json.load(json_file)

    return render(request, 'LeafletMaps/uk_cumulative_cases.html', context={'geo_data' : geo_data})
