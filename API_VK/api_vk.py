import secret
import requests
import datetime
import os
from tqdm import tqdm
from pprint import pprint

VK_TOKEN = secret.VK_TOKEN


# https://api.vk.com/method/status.get?<PARAMS>
class VKAPIClient:
    """" VK API client """
    API_BASE_URL = 'https://api.vk.com/method'

    def __init__(self, user_id, token=VK_TOKEN):
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
        if self.get_user_info().get('response'):
            return self.get_user_info()['response'][0]['id']
        else:
            print(self.get_user_info())

    def get_photos_info(self, album_id='profile'):
        """Get photo from VK"""
        params = self.get_common_params()
        params.update({
            'owner_id': self.get_int_user_id(self.user_id),
            'album_id': album_id,
            'extended': 1
        })
        response = requests.get(self._build_url('photos.get'), params=params)
        return response.json()['response']['items']

    def get_large_photos(self, album_id='profile', count=5):
        large_photo_urls = []
        for photos in self.get_photos_info(album_id):
            large_photo_urls.append({
                'likes': photos['likes']['count'],
                'create_date': datetime.datetime.fromtimestamp(photos['date']).strftime('%d-%m-%Y'),
                'url': photos['sizes'][-1]['url'],
                'size': photos['sizes'][-1]['type']
            })
        return large_photo_urls[-count:]


class LargePhoto:
    def __init__(self, user_id, count_for_save=5):
        self.user_id = user_id
        self.photos = VKAPIClient(user_id).get_large_photos(count=count_for_save)

    def _download(self, path_to_dir):
        print(f'Началась загрузка файлов')
        for photo in tqdm(self.photos, ncols=80, desc='Downloading...'):
            file_name = f"{photo['likes']}"
            if os.path.isfile(path_to_dir + os.sep + file_name + '.jpg'):
                file_name += f"-{photo['create_date']}"
            response = requests.get(photo['url'])
            with open(
                    f"{path_to_dir}{os.sep}{file_name}.jpg",
                    'wb'
            ) as file:
                file.write(response.content)

    def save_to_dir(self):
        path_to_dir = os.path.join(f"{os.getcwd()}{os.sep}files")
        if os.path.exists(path_to_dir):
            self._download(path_to_dir)
        else:
            os.makedirs(path_to_dir)
            self._download(path_to_dir)


            #
            #
            # url_for_upload = f'{url_base}/v1/disk/resources/upload'
            # params = {
            #     'path': f'98/{image_name}'
            # }
            # response = requests.get(url_for_upload,
            #                         params=params,
            #                         headers=headers)
            # current_url_upload = response.json().get('href')
            # with open(image_name, 'rb') as file:
            #     response = requests.put(current_url_upload, files={"file": file})
            #     print(response.status_code)


if __name__ == '__main__':
    # vk_client = VKAPIClient('arbuzov.producer')
    # print(vk_client.get_user_info())
    user_ph = LargePhoto('id60453017')
    user_ph.save_to_dir()
