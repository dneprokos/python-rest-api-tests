from api.genres_requests import GenresRequests
from assertpy import soft_assertions


def test_search_genres_all_parameters(admin_user_token):
    # Arrange
    searchParams = {
        "name": "Action",
        "page": 1,
        "limit": 1
    }

    # Act
    response = GenresRequests().search_genres(admin_user_token, searchParams)
    print(response.content)

    # Assert
    assert response.status_code == 200
    response_body = response.json()
    assert response_body is not None
    with soft_assertions():
        assert response_body.get("page_number") == searchParams.get("page")
        assert response_body.get("page_limit") == searchParams.get("limit")
        assert response_body.get("total_results") >= 1

        # verift that data elements count greater or eqqual to limit
        assert len(response_body.get("data")) >= searchParams.get("limit")
