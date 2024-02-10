import requests
import time

uk_city_list = ['Leeds', 'London', 'Liverpool', 'Manchester', 'Oxford', 'Edinburgh', 'Norwich', 'York']
api_key = '65c7ba131bacb131822687vay2e9196'
url = 'https://geocode.maps.co/'
path_reverse = '/reverse'


def find_uk_city(coordinates: list) -> str:
    for coordinate in coordinates:
        params = {
            'lat': coordinate[0],
            'lon': coordinate[1],
            'api_key': api_key,
        }
        response = requests.get(f'{url}{path_reverse}', params=params)
        city = response.json()['address']['city']
        if city in uk_city_list:
            vacation_city = response.json()['address']['city']
            return vacation_city
        time.sleep(1)


print(find_uk_city([
        ('55.7514952', '37.618153095505875'),
        ('52.3727598', '4.8936041'),
        ('53.4071991', '-2.99168')
    ]))
