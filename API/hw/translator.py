from dict_api_key import dict_api_key
from pprint import pprint


import requests

url = 'https://dictionary.yandex.net/api/v1/dicservice.json/lookup'
token = dict_api_key


def translate_word(word):
    params = {
        'key': dict_api_key,
        'text': word,
        'lang': 'ru-en',

    }
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.post(url, params=params, headers=headers)
    trans_word = response.json()['def'][0]['tr'][0]['text']
    return trans_word


# if __name__ == '__main__':
#     word = 'машина'
#     assert translate_word(word) == 'car'
