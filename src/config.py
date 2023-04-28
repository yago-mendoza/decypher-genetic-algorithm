import json
import string

from src.utils import bit_array


def load_config(file_path="data/input/config.json"):
    """Loads the configuration settings from a JSON file and returns them as a dictionary.

    Args:
        file_path (str, optional): The path to the JSON file to load. Defaults to "data/input/config.json".

    Returns:
        dict: A dictionary containing the configuration settings.
    """
    with open(file_path) as f:
        data = json.load(f)

    # Extract target_passwords, target_index, and parameters
    target_index = data["target_index"]
    parameters = data["parameters"]
    show_plot = data["show_plot"]
    translate_to_bits = data["translate_to_bits"]

    if translate_to_bits:
        target_passwords = [bit_array(target_password) for target_password in data["target_passwords"]]
        charset = "01"
    else:
        target_passwords = data["target_passwords"]
        charset = string.digits + string.punctuation + string.ascii_letters

    # Add target_passwords, target_index, parameters, and charset to the config_data dictionary
    config_data = {
        "translate_to_bits": translate_to_bits,
        "target_passwords": target_passwords,
        "target_index": target_index,
        "parameters": parameters,
        "show_plot": show_plot,
        "charset": charset
    }

    return config_data

config_data = load_config()