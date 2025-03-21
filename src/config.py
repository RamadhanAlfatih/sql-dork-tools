import yaml
import os

def load_config():
    """
    Load configuration from settings.yaml.
    """
    config_path = os.path.join("config", "settings.yaml")
    with open(config_path, "r") as file:
        return yaml.safe_load(file)