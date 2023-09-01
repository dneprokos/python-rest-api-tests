from api.genres_requests import GenresRequests
from assertpy import soft_assertions
from helpers.file_reader import read_json_file


def test_create_genre_from_payload_object(admin_user_token):
    # Arrange
    genre_name = "Drama"
    payload = {
        "name": genre_name
    }

    # Act
    response = GenresRequests().post_genre(admin_user_token, payload)

    # Assert
    assert response.status_code == 201
    response_body = response.json()
    assert response_body is not None

    with soft_assertions():
        assert response_body.get('id') is not None
        assert response_body.get('name') == genre_name

def test_create_genre_from_json_file(admin_user_token):
    # Arrange
    payload = read_json_file("create_genre.json")

    # Act
    response = GenresRequests().post_genre(admin_user_token, payload)

    # Assert
    assert response.status_code == 201
    response_body = response.json()
    assert response_body is not None

    with soft_assertions():
        assert response_body.get('id') is not None
        assert response_body.get('name') == payload.get('name')
