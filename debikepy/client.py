import httpx
from tzlocal import get_localzone_name

from debikepy.endpoints.mybike import bike_from_dict
from debikepy.endpoints.profile import profile_to_dict


class Client():
    def __init__(self, proxies, disable_ssl, google_api_key, refresh_token):
        self.client = httpx.Client(
            proxies=proxies,
            verify=not disable_ssl,
            headers={
                'user-agent': 'okhttp/4.9.1',
                'x-device-app-build': '41123',
                'x-device-app-identifier': 'com.conneqtech.decathlon',
                'x-device-app-language': 'fr',
                'x-device-app-version': '15.11.0',
                'x-device-language': 'fr',
                'x-device-model': 'LGE Nexus 5X',
                'x-device-platform': 'android',
                'x-device-platform-version': '27',
                'x-device-timezone': get_localzone_name(),
                'x-original-uri': 'http://subs.conneq.tech/',
                'x-token-lifetime': '600',
            }
        )

        self.refresh_token = refresh_token
        self.google_api_key = google_api_key
        self.token = ""


    def get_profile(self):
        res = self.client.request("https://decathlon.api.bike.conneq.tech/user/me",
                            headers={"authorization": f"Bearer {self.token}"})
        return res.json()

    def get_bike_type(self, id):
        res = self.client.request("https://decathlon.api.bike.conneq.tech/bike-type/" + id,
                            headers={"authorization": f"Bearer {self.token}"})
        return res.json()

    def get_bikes(self):
        res = self.client.request("https://decathlon.api.bike.conneq.tech/bike",
                            headers={"authorization": f"Bearer {self.token}"})
        return res.json()

    def get_geofences(self, bike_id):
        res = self.client.request("https://decathlon.api.bike.conneq.tech/bike/" + bike_id + "geofence",
                            headers={"authorization": f"Bearer {self.token}"})
        return res.json()

    def auth(self):
        self.profile = profile_to_dict(self.get_profile())
        self.bikes = bike_from_dict(self.get_bikes())

