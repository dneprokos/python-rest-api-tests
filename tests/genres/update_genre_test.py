from api.genres_requests import GenresRequests
from helpers.data_helper import create_random_genre
from assertpy import soft_assertions
from helpers.random_helper import generate_random_string


def test_update_valid_genre(admin_user_token):
    # Arrange
    created_genre = create_random_genre(admin_user_token)
    id = created_genre.get("id")

    # Act
    payload = {
        "name": generate_random_string(10)
    }

    response = GenresRequests().put_genre(admin_user_token, id, payload)
    print(response.text)

    # Assert
    assert response.status_code == 200
    response_body = response.json()
    with soft_assertions():
        assert response_body is not None
        assert response_body.get("id") == id
        assert response_body.get("name") == payload.get("name")
    
    # Cleanup
    GenresRequests().delete_genre(admin_user_token, id)