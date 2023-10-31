# -*- coding: utf-8 -*-

import requests

BASE_URL = "https://api.euskadi.eus/appcont/meteorologia/meteodat/images/{number:02}.png"

def download():
    for number in range(50):
        res = requests.get(BASE_URL.format(number=number))
        with open(f'images/{number:02}.png', 'wb') as fp:

            fp.write(res.content)


if __name__ == '__main__':
    download()
