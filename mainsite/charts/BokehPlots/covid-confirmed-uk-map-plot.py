from uk_covid19.api_interface import StructureType
from libs.choropleth_chart import ChoroplethChart

from uk_covid19 import Cov19API
import geopandas

all_nations = [
    "areaType=utla",
]

cases_and_deaths: StructureType = {
    "date": "date",
    "areaName": "areaName",
    "areaCode": "areaCode",
    "newCasesByPublishDate": "newCasesByPublishDate",
    "cumCasesByPublishDate": "cumCasesByPublishDate",
    "newDeathsByDeathDate": "newDeathsByDeathDate",
    "cumDeathsByDeathDate": "cumDeathsByDeathDate"
}

api = Cov19API(
    filters=all_nations,
    structure=cases_and_deaths,
    latest_by="newCasesByPublishDate"
)

df = api.get_dataframe()

geo_df = geopandas.read_file('geodata/Counties_and_Unitary_Authorities__December_2019__Boundaries_UK_BUC.geojson')

merged_df = geopandas.GeoDataFrame(df.merge(geo_df, right_on='ctyua19cd', left_on='areaCode'))

# Set the coordinate reference system EPSG:4326 (WGS84 Lat/Long)
merged_df.crs = 'epsg:4326'

# Tell GeoPandas that the column named geometry contains the points describing the countries
merged_df.set_geometry('geometry')

merged_df.to_file('uk_covid_data.geojson', driver='GeoJSON')

# Setup the tooltips
tooltips = [('Area', '@areaName'),
            ('Confirmed', '@cumCasesByPublishDate')]

choropleth = ChoroplethChart('Confirmed UK Map Plot', tooltips, 'cumCasesByPublishDate', 'Blues', 'blue', merged_df)
