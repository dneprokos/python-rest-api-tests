import requests
from api.authorization_requests import AuthorizationRequests
import re
from assertpy import assert_that, soft_assertions


def test_post_authorization_with_valid_non_admin_creds():
    """Test POST /authorization with valid non-admin credentials"""
    # Arrange
    username = 'test'
    password = 'testpassword'

    # Act
    response = AuthorizationRequests().post_authorization(username, password)

    # Assert
    with soft_assertions():
        assert_that(response.status_code).is_equal_to(requests.codes.OK)

        content_type = response.headers.get('Content-Type', '')
        assert re.match(r'^application/json(; charset=.+)?$', content_type)

        response_body = response.json()
        assert_that(response_body.get('accessToken')
                    ).is_not_none().is_not_empty()
