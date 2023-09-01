from api.genres_requests import GenresRequests
from cerberus import Validator

def test_get_genre_by_id_with_schema_validation(admin_user_token):
    # Arrange
    id = 1
    schema = {
        "name" : {"type": "string"},
        "id" : {"type": "integer"}
    }

    # Act
    response = GenresRequests().get_genre_by_id(admin_user_token, id)

    # Assert
    assert response.status_code == 200
    assert Validator(schema).validate(response.json()) == True
    