import json

# ConfigHelper class is used to work with config.json file
class ConfigHelper:
    def __init__(self, config_file_path="config.json"):
        self.config_file_path = config_file_path
        self.config_data = self.load_config()

    # load_config method is used to load config.json file
    def load_config(self):
        with open(self.config_file_path) as config_file:
            return json.load(config_file)
    
    # get_base_url method is used to get base_url from config.json file
    def get_base_url(self):
        base_url = self.config_data.get("base_url")
        assert '/api' in base_url, "base_url must contain /api"
        return base_url.rstrip("/")