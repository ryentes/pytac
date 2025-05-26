import requests
import time

class TacticusClient(object):
    __last_req_timestamp=time.time()
    __min_req_interval=1

    def __init__(self, api_key, base_url="https://api.tacticusgame.com/"):
        self.api_key=api_key
        self.base_url=base_url
    
    @property
    def api_key(self):
        return(self._api_key)
    
    @api_key.setter
    def api_key(self, api_key):
        self._api_key=api_key

    @property
    def base_url(self):
        return(self._base_url)
    
    @base_url.setter
    def base_url(self, base_url):
        self._base_url=base_url

    def get(self, url, headers, params=None):
        interval = time.time()-self.__last_req_timestamp

        # wait if the api has been called too recently
        if interval < self.__min_req_interval:
            time.sleep(self.__min_req_interval-interval)
        
        response = requests.get(
            url=url,
            headers=headers,
            params=params
        )

        if response.status_code==200:
            return(response)
        else: return("error")

    def get_player_data(self):

        headers={
            "X-API-Key": self.api_key,
            "content-type": "application/json"
        }

        url=f"{self.base_url}/api/v1/player"

        player_data=self.get(
            url=url,
            headers=headers
        )

        return(player_data)
