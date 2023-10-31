# -*- coding: utf-8 -*-
from copy import deepcopy
import json
import jwt
import requests
import time
import datetime
import os

BASE_URL = 'https://api.euskadi.eus/'

city_url = "euskalmet/weather/regions/basque_country/zones/{zone}/locations/{city}"
forecast_url = "/forecast/trends/at/{year}/{month}/{day}/for/{forecastday}"

def load_file(filename):
    with open(filename, 'r') as fp:
        return fp.read()

CITIES_TO_PROCESS = [
    {'city': 'eibar', 'zone': 'cantabrian_valleys'},
    {'city': 'antzuola', 'zone': 'cantabrian_valleys'},
]


def process_results(input):
    output = deepcopy(input)
    trendsByDate = []
    for item in output.get('trendsByDate', {}).get('set', []):
        id = item.get('weather', {}).get('id', '')
        item['weather']['icon_name'] = f'{id}.png'
        trendsByDate.append(item)
    output['trendsByDate'] = trendsByDate

    return output

def main():

    email = os.environ.get('EUSKALMET_API_EMAIL')
    private_key = os.environ.get('EUSKALMET_API_PRIVATE_KEY')

    assert bool(email)
    assert bool(private_key)

    claim_set = {
        "aud": "met01.apikey",
        "iss": "sampleApp",
        "exp": int(time.time() + (60 * 60)),
        "version": "1.0.0",
        "iat": int(time.time()),
        "email": email,
    }
    bearer_token = jwt.encode(claim_set, private_key_algorithm="RS256")

    today = datetime.datetime.now()
    year = today.year
    month = today.month
    day = today.day

    tomorrow = today + datetime.timedelta(days=1)

    forecastday = f'{tomorrow.year}{tomorrow.month:02}{tomorrow.day:02}'

    for item in CITIES_TO_PROCESS:
        assert 'zone' in item
        assert 'city' in item
        url = f'{BASE_URL}{city_url}{forecast_url}'.format(
            year=year,
            month=month,
            day=day,
            forecastday=forecastday,
            zone=item['zone'],
            city=item['city'],
        )
        print(f"Downloading forecast: {item['city']} {forecastday} ")

        result = requests.get(
            url,
            headers={
                "Authorization": f"Bearer {bearer_token}"
            },
        )
        if result.ok:
            results_json = result.json()
            processed_results = process_results(results_json)
            with open(f'forecasts/{item["city"]}-euskalmet.json', 'w') as fp:
                json.dump(processed_results, fp)
        else:
            print(f"ERROR code: {result.status_code}")
            print(result.text)



if __name__ == "__main__":
    main()
