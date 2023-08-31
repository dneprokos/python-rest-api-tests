import pip._vendor.requests
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
    with soft_assertions(): # soft_assertions() allows us to continue to run the test even if one of the assertions fails
        assert_that (response.status_code).is_equal_to(pip._vendor.requests.codes.OK)
        content_type_header = response.headers.get('Content-Type', '')
        assert re.match(r'^application/json(; charset=.+)?$', content_type_header)
        responseBody = response.json()
        assert responseBody['accessToken'] is not None
        assert responseBody['accessToken'] != ''