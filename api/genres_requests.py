from ._base_api import BaseRequests
import pip._vendor.requests

class GenresRequests(BaseRequests):
    def __init__(self):
        super().__init__()
        self.base_url += '/genres'

    # Get all genres
    def get_genres(self, auth_token: str):
        url = f"{self.base_url}"
        headers = {
            "Accept": "application/json",
            "Authorization": f"Bearer {auth_token}"
        }

        response = pip._vendor.requests.get(url, headers=headers)

        return response

    # Get genre by id
    def get_genre_by_id(self, auth_token: str, genre_id: int):
        url = f"{self.base_url}/{genre_id}"
        headers = {
            "Accept": "application/json",
            "Authorization": f"Bearer {auth_token}"
        }

        response = pip._vendor.requests.get(url, headers=headers)

        return response
    
    # Create genre
    def post_genre(self, auth_token: str, payload: dict[str, any]):
        url = f"{self.base_url}"
        headers = {
            "Accept": "application/json",
            "Authorization": f"Bearer {auth_token}"
        }

        response = pip._vendor.requests.post(url, headers=headers, json=payload)

        return response
    
    # Create genres - bulk
    def post_genre_bulk(self, auth_token: str, payload: list[dict[str, any]]):
        url = f"{self.base_url}/bulk"
        headers = {
            "Accept": "application/json",
            "Authorization": f"Bearer {auth_token}"
        }

        response = pip._vendor.requests.post(url, headers=headers, json=payload)

        return response
    
    # Update genre
    def put_genre(self, auth_token: str, genre_id: int, payload: dict[str, any]):
        url = f"{self.base_url}/{genre_id}"
        headers = {
            "Accept": "application/json",
            "Authorization": f"Bearer {auth_token}"
        }

        response = pip._vendor.requests.put(url, headers=headers, json=payload)

        return response
    
    # Delete genre
    def delete_genre(self, auth_token: str, genre_id: int):
        url = f"{self.base_url}/{genre_id}"
        headers = {
            "Accept": "application/json",
            "Authorization": f"Bearer {auth_token}"
        }

        response = pip._vendor.requests.delete(url, headers=headers)

        return response
    
    def search_genres(self, auth_token: str, queryParams: dict[str, any] = {}):
        url = f"{self.base_url}/genres/search"
        headers = {
            "Accept": "application/json",
            "Authorization": f"Bearer {auth_token}"
        }

        response = pip._vendor.requests.get(url, params=queryParams, headers=headers)

        return response.json()