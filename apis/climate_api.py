import requests
import os
from pprint import pprint
from .conversion_dicts import months_int
from database.model import Trip

key = os.environ.get('CLIMATE_KEY')







url = 'https://api.meteostat.net/v2/point/climate'

"""This is the only function in this module that should be called from other modules"""
def get_weather_data(park, month):
    month_int = _get_month_int(month.upper())
    response = _climate_api_call(park.latitude, park.longitude)
    trip_with_climate = _add_climate_data_to_trip(response, park, month_int)
    return trip_with_climate
    
    
def _get_month_int(month):
    month_int = months_int[month]
    return month_int


def _climate_api_call(latitude, longitude):
    params = {'lat' : latitude, 'lon' : longitude}
    headers={'x-api-key': key}
    response = requests.get(url, params=params, headers=headers).json()
    return response


def _add_climate_data_to_trip(response, park, month):
    data = response['data']
    climate_for_month = data[month - 1]
    precipitation = _convert_mm_to_inches(climate_for_month['prcp'])
    avg_temp = _convert_celsius_to_fahrenheit(climate_for_month['tavg'])
    max_temp = _convert_celsius_to_fahrenheit(climate_for_month['tmax'])
    min_temp = _convert_celsius_to_fahrenheit(climate_for_month['tmin'])

    trip = Trip(month= month, park= park, precipitation= precipitation, avg_temp = avg_temp, max_temp= max_temp, min_temp= min_temp)

    return trip


def _convert_celsius_to_fahrenheit(temp):
    try:
        temperature = round((float(temp) * 1.8) + 32, 2)
    except:
        temperature = 0
    return temperature


def _convert_mm_to_inches(rainfall):
    try:
        precipitation = round(float(rainfall) / 25.4, 1)
    except:
        precipitation = 0
    return precipitation



