from api.genres_requests import GenresRequests
from helpers.data_helper import create_random_genre


def test_delete_genre_with_valid_id(admin_user_token):
    # Arrange
    created_genre = create_random_genre(admin_user_token)
    genre_id = created_genre.get('id')

    # Act
    response = GenresRequests().delete_genre(admin_user_token, genre_id)

    # Assert
    assert response.status_code == 204
    assert GenresRequests().get_genre_by_id(admin_user_token, genre_id).status_code == 404
    