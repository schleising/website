from datetime import datetime
import requests

from django.core.cache import cache

# The URL containing the data
json_url = 'https://pomber.github.io/covid19/timeseries.json'

def GetGlobalData():
    header = requests.head(json_url)
    cached_header = cache.get('global-data-last-update')
    raw_data = cache.get('global-data')

    if cached_header == None:
        if header.status_code == 200:
            cache.set('global-data-last-update', header)
            cached_header = cache.get('global-data-last-update')
            print('Header Set')

    if raw_data == None:
        raw_data = requests.get(json_url)

        if raw_data.status_code == 200:
            cache.set('global-data', raw_data)
            print('Raw Data Set')

    if header.status_code == 200:
        cache_modified  = datetime.strptime(cached_header.headers['Last-Modified'], '%a, %d %b %Y %H:%M:%S %Z')
        latest_modified = datetime.strptime(header.headers['Last-Modified'], '%a, %d %b %Y %H:%M:%S %Z')

        print()
        print(cache_modified)
        print(latest_modified)
        print()

        if latest_modified > cache_modified:
            cache.set('global-data-last-update', header)
            raw_data = requests.get(json_url)

            if raw_data.status_code == 200:
                cache.set('global-data', raw_data)
                print('Cache Updated')
            
            else:
                raw_data = cache.get('global-data')
                print('Bad Data Response')
        
        else:
            raw_data = cache.get('global-data')
            print('Cache Used')
    else:
        raw_data = cache.get('global-data')
        print('Bad Header Response')

    json_data = raw_data.json()

    return json_data
