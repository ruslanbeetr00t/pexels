import requests
import json
from api_pexels import API


headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0',
           'Authorization': API
           }


def search_input():
    search = input('write something')
    page = int(input('add number page'))
    return search, page


def parameter_url():
    user_search = search_input()
    url = f'https://api.pexels.com/v1/search?query={user_search[0]}&per_page={user_search[1]}'
    return url


def send_url():
    try:
        response = requests.get(parameter_url(), headers=headers, timeout=10)
        if response.status_code == 200:
            print(response.json())
            print(response.headers['X-Ratelimit-Remaining'])
            return response.json()
    except requests.exceptions.Timeout:
        print('Ви занадто довго чекаете, або сервер невідповідае :) ')
        return send_url()
    except requests.exceptions.RequestException as e:
        print(e)


send_url()

