from api.genres_requests import GenresRequests
from assertpy import soft_assertions
from cerberus import Validator


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

def test_search_genres_all_parameters_with_schema_validation(admin_user_token):
    # Arrange
    searchParams = {
        "name": "Action",
        "page": 1,
        "limit": 1
    }

    response_schema = {
        "page_number": {"type": "integer"},
        "page_limit": {"type": "integer"},
        "total_results": {"type": "integer"},
        "data": {"type": "list"}
    }

    data_item_schema = {
        "name": {"type": "string"},
        "id": {"type": "integer"}
    }

    # Act
    response = GenresRequests().search_genres(admin_user_token, searchParams)

    # Assert
    assert response.status_code == 200
    response_body = response.json()
    assert response_body is not None
    with soft_assertions():
        assert Validator(response_schema).validate(response_body) == True
        for item in response_body.get("data"):
            assert Validator(data_item_schema).validate(item) == True
