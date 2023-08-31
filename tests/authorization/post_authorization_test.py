from api.authorization_requests import AuthorizationRequests
import re


def test_post_authorization_with_valid_non_admin_creds():
    """Test POST /authorization with valid non-admin credentials"""
    # Arrange
    username = 'test'
    password = 'testpassword'

    # Act
    response = AuthorizationRequests().post_authorization(username, password)

    # Assert
    assert response.status_code == 200
    content_type_header = response.headers.get('Content-Type', '')
    assert re.match(r'^application/json(; charset=.+)?$', content_type_header)
    responseBody = response.json()
    assert responseBody['accessToken'] is not None
    assert responseBody['accessToken'] != ''