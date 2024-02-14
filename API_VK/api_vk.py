import secret
import requests
import datetime
from pprint import pprint

VK_TOKEN = secret.VK_TOKEN


# https://api.vk.com/method/status.get?<PARAMS>
class VKAPIClient:
    """" VK API client """
    API_BASE_URL = 'https://api.vk.com/method'

    def __init__(self, token, user_id):
        self.token = token
        self.user_id = user_id

    def get_common_params(self):
        """
        Get common params for VK API all requests
        return: access_token, API version
        """
        return {
            'access_token': self.token,
            'v': '5.131'
        }

    def _build_url(self, api_method):
        """build VK API url"""
        return f'{self.API_BASE_URL}/{api_method}'

    def get_user_info(self):
        """Get user information from VK API"""
        params = self.get_common_params()
        params.update({
            'user_id': self.user_id
        })
        response = requests.get(self._build_url('users.get'), params=params)
        return response.json()

    def get_int_user_id(self, user_id):
        """Get integer user id from VK API by user_id"""
        return self.get_user_info()['response'][0]['id']

    def get_photos_info(self, album_id):
        """Get photo from VK"""
        params = self.get_common_params()
        params.update({
            'owner_id': self.get_int_user_id(self.user_id),
            'album_id': album_id,
            'extended': 1
        })
        response = requests.get(self._build_url('photos.get'), params=params)
        return response.json()['response']['items']

    def get_large_photos(self, album_id):
        large_photo_urls = []
        for photos in self.get_photos_info(album_id):
            large_photo_urls.append({
                'likes': photos['likes']['count'],
                'create_date': datetime.datetime.fromtimestamp(photos['date']).strftime('%d-%m-%Y'),
                'url': photos['sizes'][-1]['url'],
                'size': photos['sizes'][-1]['type']
            })
        return large_photo_urls


if __name__ == '__main__':
    vk_client = VKAPIClient(VK_TOKEN, 'arbuzov.producer')
    print(vk_client.get_user_info())
    pprint(vk_client.get_large_photos('profile'))
