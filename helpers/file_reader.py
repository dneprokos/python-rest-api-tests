import json
from pathlib import Path

DATA_FOLDER = Path(__file__).parent.parent / "data"

# Read a JSON file and return a dictionary
def read_json_file(file_name: str): # file_name is a string with extension
    file_path = DATA_FOLDER / file_name
    with open(file_path, 'r') as file:
        return json.load(file)