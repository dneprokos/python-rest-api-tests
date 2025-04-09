from ._base_api import BaseRequests
import requests


class AuthorizationRequests(BaseRequests):
    def __init__(self):
        """
        Initializes the AuthorizationRequests class by setting the base URL
        for the authorization endpoint.
        """
        super().__init__()
        self.base_url += '/authorization'

    def post_authorization(self, username: str, password: str):
        """
        Sends a POST request to the authorization endpoint with the provided credentials.

        Args:
            username (str): The user's username.
            password (str): The user's password.

        Returns:
            Response: The HTTP response object containing the authorization token or error message.
        """
        url = self.base_url
        headers = {
            "Accept": "application/json"
        }
        params = {
            "username": username,
            "password": password
        }

        response = requests.post(url, headers=headers, params=params)

        return response
