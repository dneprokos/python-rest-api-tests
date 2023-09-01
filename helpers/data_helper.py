from api.genres_requests import GenresRequests
from helpers.random_helper import generate_random_string

# This function creates a new random genre and returns the response body
def create_random_genre(token):
    payload = {
        "name": generate_random_string(10)
    }

    response = GenresRequests().post_genre(token, payload)
    assert response.status_code == 201
    response_body = response.json()
    assert response_body is not None
    assert response_body["id"] is not None
    assert response_body["id"] > 0
    return response_body