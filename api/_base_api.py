from helpers.config_helper import ConfigHelper

class BaseRequests:
    def __init__(self):
        self.base_url = ConfigHelper().get_base_url()