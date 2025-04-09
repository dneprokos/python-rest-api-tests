from ._base_api import BaseRequests
from requests.models import Response
import logging

logger = logging.getLogger(__name__)


class GenresRequests(BaseRequests):
    def __init__(self):
        """
        Initializes the GenresRequests class by setting the base URL
        for genre-related API requests.
        """
        super().__init__()
        self.base_url += '/genres'

    def get_all_genres(self, auth_token: str):
        """
        Retrieves a list of all genres from the API.

        Args:
            auth_token (str): The Bearer token for authorization.

        Returns:
            Response: The HTTP response object from the GET request.
        """
        url = f"{self.base_url}"
        headers = self.setup_headers(auth_token)
        return self.get_request(url, headers)

    def get_all_genres_return_xml_hardcoded(self, auth_token: str):
        """
        Returns a hardcoded XML representation of genres.
        Used only for testing XML responses.

        Args:
            auth_token (str): The Bearer token for authorization.

        Returns:
            Response: A mocked HTTP response with XML content.
        """
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

    def get_genre_by_id(self, auth_token: str, genre_id: int):
        """
        Retrieves a genre by its ID.

        Args:
            auth_token (str): The Bearer token for authorization.
            genre_id (int): The ID of the genre to retrieve.

        Returns:
            Response: The HTTP response object from the GET request.
        """
        url = f"{self.base_url}/{genre_id}"
        headers = self.setup_headers(auth_token)
        return self.get_request(url, headers)

    def post_genre(self, auth_token: str, payload: dict[str, any]):
        """
        Creates a new genre.

        Args:
            auth_token (str): The Bearer token for authorization.
            payload (dict): A dictionary containing genre data.

        Returns:
            Response: The HTTP response object from the POST request.
        """
        url = f"{self.base_url}"
        headers = self.setup_headers(auth_token)
        return self.post_request(url, payload, headers)

    def post_genre_bulk(self, auth_token: str, payload: list[dict[str, any]]):
        """
        Creates multiple genres in bulk.

        Args:
            auth_token (str): The Bearer token for authorization.
            payload (list): A list of dictionaries with genre data.

        Returns:
            Response: The HTTP response object from the POST request.
        """
        url = f"{self.base_url}/bulk"
        headers = self.setup_headers(auth_token)
        return self.post_request(url, payload, headers)

    def put_genre(self, auth_token: str, genre_id: int, payload: dict[str, any]):
        """
        Updates an existing genre by its ID.

        Args:
            auth_token (str): The Bearer token for authorization.
            genre_id (int): The ID of the genre to update.
            payload (dict): The updated genre data.

        Returns:
            Response: The HTTP response object from the PUT request.
        """
        url = f"{self.base_url}/{genre_id}"
        headers = self.setup_headers(auth_token)
        return self.put_request(url, payload, headers)

    def delete_genre(self, auth_token: str, genre_id: int):
        """
        Deletes a genre by its ID.

        Args:
            auth_token (str): The Bearer token for authorization.
            genre_id (int): The ID of the genre to delete.

        Returns:
            Response: The HTTP response object from the DELETE request.
        """
        url = f"{self.base_url}/{genre_id}"
        headers = self.setup_headers(auth_token)
        return self.delete_request(url, headers)

    def search_genres(self, auth_token: str, queryParams: dict[str, any] = {}):
        """
        Searches genres based on query parameters.

        Args:
            auth_token (str): The Bearer token for authorization.
            queryParams (dict): Optional query parameters for filtering.

        Returns:
            Response: The HTTP response object from the GET request with parameters.
        """
        url = f"{self.base_url}/search"
        headers = self.setup_headers(auth_token)
        return self.get_request_with_params(url, queryParams, headers)
