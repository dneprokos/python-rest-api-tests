from ._base_api import BaseRequests
import pip._vendor.requests
import requests
from requests.models import Response

class GenresRequests(BaseRequests):
    def __init__(self):
        super().__init__()
        self.base_url += '/genres'

    # Get all genres
    def get_all_genres(self, auth_token: str):
        url = f"{self.base_url}"
        headers = {
            "Accept": "application/json",
            "Authorization": f"Bearer {auth_token}"
        }

        response = pip._vendor.requests.get(url, headers=headers)

        return response
    
    # Get all genres - return xml hardcoded. This is just for testing purposes
    def get_all_genres_return_xml_hardcoded(self, auth_token: str):
        genres = [
            {"id": 1, "name": "Action"},
            {"id": 2, "name": "Horror"},
            {"id": 3, "name": "Romance"},
            {"id": 4, "name": "Science Fiction"},
            {"id": 5, "name": "Disaster Film"},
            {"id": 6, "name": "Epic Romance"},
            {"id": 7, "name": "Superhero Film"},
            {"id": 8, "name": "Space Western"},
            {"id": 9, "name": "Comedy"},
            {"id": 10, "name": "Adventure"},
            {"id": 11, "name": "Western"}
        ]
    
        xml_str = '<?xml version="1.0" encoding="UTF-8"?>\n'
        xml_str += '<genres>\n'

        for genre in genres:
            xml_str += '  <genre>\n'
            xml_str += f'    <id>{genre["id"]}</id>\n'
            xml_str += f'    <name>{genre["name"]}</name>\n'
            xml_str += '  </genre>\n'

        xml_str += '</genres>'

        response = Response()
        response._content = xml_str.encode('utf-8')
        response.status_code = 200
        response.headers = {'Content-Type': 'application/xml'}
        
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