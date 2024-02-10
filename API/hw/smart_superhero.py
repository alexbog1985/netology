# Есть API по информации о супергероях с информацией по всем супергероям.
# Теперь нужно найти самого умного супергероя среди списка супергеров.
#
# Напишите функцию get_the_smartest_superhero,
# которая принимает на вход список superheros, состоящий из id.


import requests


def get_the_smartest_superhero(superheros):
    base_url = "https://akabab.github.io/superhero-api/api/"
    the_smartest_superhero = ''
    intelligence = 0

    for superhero in superheros:
        url = f'{base_url}/id/{superhero}.json'
        response = requests.get(url)
        if response.status_code == 200:
            if response.json()['powerstats']['intelligence'] > intelligence:
                the_smartest_superhero = response.json()['name'], response.json()['powerstats']['intelligence']
                intelligence = response.json()['powerstats']['intelligence']
        else:
            print(f'Ошибка, возможно героя с id: {superhero} не существует')
    return the_smartest_superhero


print(get_the_smartest_superhero([1, 2, 3]))
