import secret
import requests
from pprint import pprint

VK_TOKEN = secret.VK_TOKEN


# https://api.vk.com/method/status.get?<PARAMS>
class VKAPIClient:
    API_BASE_URL = 'https://api.vk.com/method'

    def __init__(self, token, user_id):
        self.token = token
        self.user_id = user_id

    def get_common_params(self):
        return {
            'access_token': self.token,
            'v': '5.131'
        }

    def get_status(self):
        params = self.get_common_params()
        params.update({'user_id': self.user_id})
        response = requests.get(
            f'{self.API_BASE_URL}/status.get', params=params)
        return response.json()

    def get_user_info(self):
        params = self.get_common_params()
        params.update({'user_id': self.user_id})
        response = requests.get(
            f'{self.API_BASE_URL}/users.get', params=params
        )
        return response.json()

    def get_photo(self):
        params = self.get_common_params()
        params.update({
            'owner_id': self.user_id,
            'album_id': 'profile',
            'photo_sizes': 1
        })
        response = requests.get(
            f'{self.API_BASE_URL}/photos.get', params=params
        )
        all_photos = response.json()['response']['items']
        photos = []
        for photo in all_photos:
            photos.append(photo['sizes'][-1])
        return photos


if __name__ == '__main__':
    vk_client = VKAPIClient(VK_TOKEN, '162414632')
    print(vk_client.get_user_info())
    pprint(vk_client.get_photo())
