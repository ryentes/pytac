import requests
import time
from pytac.models.Unit import Unit

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
        else: return(response.raise_for_status())

    def get_player_data(self):

        headers={
            "X-API-Key": self.api_key,
            "content-type": "application/json"
        }

        url=f"{self.base_url}/api/v1/player"

        r=self.get(
            url=url,
            headers=headers
        )

        player_data = [
            Unit.model_validate(pd) for pd in r.json().get("player").get("units")
        ]

        return(player_data)
    
    def get_guild_data(self):

        headers={
            "X-API-Key": self.api_key,
            "content-type": "application/json"
        }

        url=f"{self.base_url}/api/v1/guild"

        guild_data=self.get(
            url=url,
            headers=headers
        )

        return(guild_data)
    
    def get_guild_raid_data(self):

        headers={
            "X-API-Key": self.api_key,
            "content-type": "application/json"
        }

        url=f"{self.base_url}/api/v1/guildRaid"

        guild_raid_data=self.get(
            url=url,
            headers=headers
        )

        return(guild_raid_data)
