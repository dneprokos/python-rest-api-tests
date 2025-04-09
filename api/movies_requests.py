from ._base_api import BaseRequests


class MoviesRequests(BaseRequests):
    def __init__(self):
        """
        Initializes the MoviesRequests class by setting the base URL
        for movie-related API requests.
        """
        super().__init__()
        self.base_url += '/movies'

    def create_movie(self, auth_token: str, payload: dict[str, any]):
        """
        Creates a new movie.

        Args:
            auth_token (str): The Bearer token for authorization.
            payload (dict): A dictionary containing movie data.

        Returns:
            Response: The HTTP response object from the POST request.
        """
        url = f"{self.base_url}"
        headers = self.setup_headers(auth_token)
        return self.post_request(url, payload, headers)

    def get_movie_by_id(self, auth_token: str, movie_id: int):
        """
        Retrieves a movie by its ID.

        Args:
            auth_token (str): The Bearer token for authorization.
            movie_id (int): The ID of the movie to retrieve.

        Returns:
            Response: The HTTP response object from the GET request.
        """
        url = f"{self.base_url}/{movie_id}"
        headers = self.setup_headers(auth_token)
        return self.get_request(url, headers)

    def search_movies(self, auth_token: str, queryParams: dict[str, any] = {}):
        """
        Searches movies based on query parameters.

        Args:
            auth_token (str): The Bearer token for authorization.
            queryParams (dict): Optional query parameters for filtering.

        Returns:
            Response: The HTTP response object from the GET request with parameters.
        """
        url = f"{self.base_url}/search"
        headers = self.setup_headers(auth_token)
        return self.get_request_with_params(url, queryParams, headers)

    def delete_movie(self, auth_token: str, movie_id: int):
        """
        Deletes a movie by its ID.

        Args:
            auth_token (str): The Bearer token for authorization.
            movie_id (int): The ID of the movie to delete.

        Returns:
            Response: The HTTP response object from the DELETE request.
        """
        url = f"{self.base_url}/{movie_id}"
        headers = self.setup_headers(auth_token)
        return self.delete_request(url, headers)
