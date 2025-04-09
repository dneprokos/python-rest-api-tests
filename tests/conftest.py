import pytest
import requests
from api.authorization_requests import AuthorizationRequests
from helpers.config_helper import ConfigHelper
import logging


@pytest.fixture(scope="session")
def regular_user_token():
    """Generate token for regular user"""
    user_name, password = ConfigHelper().get_regular_user_credentials()
    response = AuthorizationRequests().post_authorization(user_name, password)
    assert response.status_code == requests.codes.OK, "Token was not generated"
    response_body = response.json()
    assert response_body is not None, "Token was not generated"
    return response_body['accessToken']


@pytest.fixture(scope="session")
def admin_user_token():
    """Generate token for admin user"""
    user_name, password = ConfigHelper().get_admin_user_credentials()
    response = AuthorizationRequests().post_authorization(user_name, password)
    assert response.status_code == requests.codes.OK, "Token was not generated"
    response_body = response.json()
    assert response_body is not None, "Token was not generated"
    return response_body['accessToken']


def pytest_runtest_logstart(nodeid, location):
    test_name = nodeid.split("::")[-1]
    logging.info(f"\n📌 Starting test: {test_name}")


def pytest_configure(config):
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s [%(levelname)s] %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
