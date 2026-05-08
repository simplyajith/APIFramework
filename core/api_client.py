import requests

from core.logdecorator import log_request
from core.logger import get_logger

logger = get_logger("APIClient")

class APIClient:
    def __init__(self,base_url,headers=None):
        self.base_url = base_url
        self.headers = headers or {}

    @log_request
    def _request(self,method,endpoint,**kwargs):
        url = f'{self.base_url}/{endpoint}'
        response = requests.request(method,
                                    url=url,
                                    headers=self.headers,
                                    **kwargs
                                    )
        return response

    def get(self,endpoint,params=None):
        return self._request("GET",endpoint,params=params)

    def post(self,endpoint,json=None):
        return self._request("POST",endpoint,json=json)

    def put(self,endpoint,json=None):
        return self._request("PUT",endpoint,json=json)

    def delete(self,endpoint):
        return self._request("DELETE",endpoint)
