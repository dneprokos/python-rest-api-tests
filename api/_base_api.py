from helpers.config_helper import ConfigHelper
import requests
import logging

logger = logging.getLogger(__name__)


class BaseRequests:
    def __init__(self):
        self.base_url = ConfigHelper().get_base_url()

    def post_request(self, url, json, headers):
        logger.info(f"POST Request to {url}")
        logger.debug(f"Headers: {self._sanitize_headers(headers)}")
        logger.debug(f"Payload: {json}")
        response = requests.post(url, json=json, headers=headers)
        logger.info(f"Response status: {response.status_code}")
        logger.debug(f"Response body: {response.text}")
        return response

    def get_request(self, url, headers):
        logger.info(f"GET Request to {url}")
        logger.debug(f"Headers: {self._sanitize_headers(headers)}")
        response = requests.get(url, headers=headers)
        logger.info(f"Response status: {response.status_code}")
        logger.debug(f"Response body: {response.text}")
        return response

    def get_request_with_params(self, url, params, headers):
        logger.info(f"GET Request to {url} with params {params}")
        logger.debug(f"Headers: {self._sanitize_headers(headers)}")
        response = requests.get(url, params=params, headers=headers)
        logger.info(f"Response status: {response.status_code}")
        logger.debug(f"Response body: {response.text}")
        return response

    def put_request(self, url, json, headers):
        logger.info(f"PUT Request to {url}")
        logger.debug(f"Headers: {self._sanitize_headers(headers)}")
        logger.debug(f"Payload: {json}")
        response = requests.put(url, json=json, headers=headers)
        logger.info(f"Response status: {response.status_code}")
        logger.debug(f"Response body: {response.text}")
        return response

    def delete_request(self, url, headers):
        logger.info(f"DELETE Request to {url}")
        logger.debug(f"Headers: {self._sanitize_headers(headers)}")
        response = requests.delete(url, headers=headers)
        logger.info(f"Response status: {response.status_code}")
        logger.debug(f"Response body: {response.text}")
        return response

    def patch_request(self, url, json, headers):
        logger.info(f"PATCH Request to {url}")
        logger.debug(f"Headers: {self._sanitize_headers(headers)}")
        logger.debug(f"Payload: {json}")
        response = requests.patch(url, json=json, headers=headers)
        logger.info(f"Response status: {response.status_code}")
        logger.debug(f"Response body: {response.text}")
        return response

    def setup_headers(self, auth_token: str):
        return {
            "Accept": "application/json",
            "Authorization": f"Bearer {auth_token}"
        }

    def _sanitize_headers(self, headers: dict) -> dict:
        """
        Redacts sensitive values like Authorization tokens for safe logging.
        """
        sanitized = headers.copy()
        if 'Authorization' in sanitized:
            sanitized['Authorization'] = 'Bearer ***'
        return sanitized
