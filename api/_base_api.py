from helpers.config_helper import ConfigHelper
import requests

class BaseRequests:
    def __init__(self):
        self.base_url = ConfigHelper().get_base_url()

    def post_request(self, url, json, headers):
        return requests.post(url, json=json, headers=headers)
    
    def get_request(self, url, headers):
        return requests.get(url, headers=headers)
    
    def get_request_with_params(self, url, params, headers):
        return requests.get(url, params=params, headers=headers)
    
    def put_request(self, url, json, headers):
        return requests.put(url, json=json, headers=headers)
    
    def delete_request(self, url, headers):
        return requests.delete(url, headers=headers)
    
    def patch_request(self, url, json, headers):
        return requests.patch(url, json=json, headers=headers)