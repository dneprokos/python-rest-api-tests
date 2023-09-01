from json import loads
from assertpy import assert_that, soft_assertions
from api.genres_requests import GenresRequests
import requests
from jsonpath_ng import parse


def test_get_all_genres_with_regular_user(regular_user_token):
    # Arrange

    # Act
    response = GenresRequests().get_all_genres(regular_user_token)

    # Assert
    assert_that(response.status_code).is_equal_to(requests.codes.OK)
    response_body = response.json()
    assert_that(response_body).is_not_empty()
    with soft_assertions(): # soft_assertions() allows us to continue to run the test even if one of the assertions fails
        # assert_that(response_body).extracting('id').is_not_none() # we can use extracting() to get a list of values for a given key
        extracted_ids = [item.get('id') for item in response_body]

        for id_value in extracted_ids:
            assert_that(id_value).is_not_none()
        
        # assert_that(response_body).extracting('name').contains('Action') # we can use contains() to check that the list contains the element
        assert_that(response_body).extracting('name').contains('Action', 'Horror', 'Romance') # we can use contains() to check that the list contains all the elements

def test_get_all_genres_parse_json_expression(admin_user_token):
    # Arrange

    # Act
    response = GenresRequests().get_all_genres(admin_user_token)

    # Assert
    assert_that(response.status_code).is_equal_to(requests.codes.OK)
    genres = loads(response.text) # loads() converts a string to a dictionary
    expression = parse('$[*].name') # parse() allows us to use JSONPath expressions to extract values from a dictionary
    genres_names = [match.value for match in expression.find(genres)] # find() returns a list of matches
    print(genres_names)
        