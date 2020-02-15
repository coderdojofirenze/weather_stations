#!/usr/bin/env python3

from requests import get
import json
from pprint import pprint

ws_base_url="https://apex.oracle.com/pls/apex/raspberrypi/weatherstation"
station_id=511059

url=f"{ws_base_url}/getlatestmeasurements/{station_id}"

weather = get(url).json()['items']
pprint(weather)

