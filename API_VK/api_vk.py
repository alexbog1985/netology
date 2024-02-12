import sys

import secret
import requests
from urllib.parse import urlencode

VK_TOKEN =


# https://api.vk.com/method/status.get?<PARAMS>
class VKAPIClient:
    API_BASE_URL = 'https://api.vk.com/method'

    def __init__(self, token, user_id):
        self.token = token
        self.owner_id = user_id

    def get_common_params(self):
        return {
            'access_token': self.token,
            'v': '5.131'
        }

    def get_status(self):
        params = self.get_common_params()
        params.update({'owner_id': self.owner_id, 'album_id': 'profile'})
        response = requests.get(
            f'{self.API_BASE_URL}/photos.get', params=params)
        return response.json()


if __name__ == '__main__':
    vk_client = VKAPIClient(VK_TOKEN, '162414632')
    print(vk_client.get_status())
