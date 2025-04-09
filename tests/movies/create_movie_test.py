from assertpy import soft_assertions
from api.movies_requests import MoviesRequests


def test_create_movie_successfully(admin_user_token):
    # Arrange
    payload = {
        "name": "Movie name",
        "release_date": 1930,
        "genre_ids": [
            1,
            2
        ]
    }

    # Act
    response = MoviesRequests().create_movie(admin_user_token, payload)

    # Assert
    assert response.status_code == 201
    body = response.json()
    with soft_assertions():
        assert body["name"] == payload["name"]
        assert body["release_date"] == payload["release_date"]
        assert body["genre_ids"] == payload["genre_ids"]
