from ._base_api import BaseRequests
import pip._vendor.requests

class AuthorizationRequests(BaseRequests):
    def __init__(self):
        super().__init__()
        self.base_url += '/authorization'

    def post_authorization(self, username: str, password: str):
        url = f"{self.base_url}?username={username}&password={password}"
        headers = {
            "Accept": "application/json"
        }

        response = pip._vendor.requests.post(url, headers=headers)

        return response