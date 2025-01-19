import json
import os

CONFIG_FILE = "config.json"

def load_configuration():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_configuration(config):
    os.system(f"attrib -h {CONFIG_FILE}")
    with open(CONFIG_FILE, 'w') as f:
        json.dump(config, f, indent=4)
    os.system(f"attrib +h {CONFIG_FILE}")