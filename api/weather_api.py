import json
import urllib.request
import urllib.error
import sys
import datetime
import uuid

def fetch_weather_data(location, start_date, end_date, api_key):
    url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}/{start_date}/{end_date}?unitGroup=metric&key={api_key}"
    try:
        response = urllib.request.urlopen(url)
    except urllib.error.HTTPError as e:
        error_info = e.read().decode()
        print('Error code:', e.code, error_info)
        sys.exit()
    except urllib.error.URLError as e:
        error_info = e.read().decode()
        print('Error code:', e.code, error_info)
        sys.exit()

    data = response.read()
    weather_data = json.loads(data.decode('utf-8'))

    resolved_address = weather_data.get('resolvedAddress')
    start_date = weather_data['days'][0]['datetime']
    query_cost = weather_data.get('queryCost')
    average_temp = weather_data['days'][0]['temp']
    cloud_cover = weather_data['days'][0]['cloudcover']
    runtime_timestamp = weather_data['days'][0]['hours'][0]['datetimeEpoch']
    created_at = datetime.datetime.now()
    weather_uuid = str(uuid.uuid4())

    return resolved_address, start_date, query_cost, average_temp, cloud_cover, runtime_timestamp, created_at, weather_uuid
