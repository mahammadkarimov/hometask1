import json

def load_config(config_file='config_file.json'):
    try:
        with open(config_file, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {"data_source": "memory"} #Default source memory