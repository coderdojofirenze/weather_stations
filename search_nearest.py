#!/usr/bin/env python3

from requests import get
import sys
import json
import geopy.distance
from pprint import pprint

my_lat = 43.798135
my_lon = 11.238411

ws_base_url='https://apex.oracle.com/pls/apex/raspberrypi/weatherstation'
get_station_url = f"{ws_base_url}/getallstations"

stations = get(get_station_url).json()['items']

min_distance = sys.float_info.max
nearest_station_id = -1
nearest_station_lat = 9999
nearest_station_lon = 9999

for station in stations:
    dist = geopy.distance.distance(
        (station['weather_stn_lat'], station['weather_stn_long']),
        (my_lat, my_lon))
    if dist < min_distance:
        min_distance = dist
        nearest_station_id = station['weather_stn_id']
        nearest_station_lat = station['weather_stn_lat']
        nearest_station_lon = station['weather_stn_long']

print(f"Nearest station found at {min_distance} with ID = {nearest_station_id}")
print(f"Latitude = {nearest_station_lat} - Longitude = {nearest_station_lon}")
print("\nWeather data:")
fetch_weather_url = f"{ws_base_url}/getlatestmeasurements/{nearest_station_id}"
weather = get(fetch_weather_url).json()['items']
pprint(weather)

