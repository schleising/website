import requests

from django.core.cache import cache

# The URL containing the data
json_url = 'https://pomber.github.io/covid19/timeseries.json'

def GetGlobalData():
    raw_data = cache.get_or_set('global-data', requests.get(json_url), 5 * 60)

    json_data = raw_data.json()

    return json_data
