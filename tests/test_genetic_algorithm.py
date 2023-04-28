import itertools
import json
import random

import pytest

from src.genetic_algorithm import genetic_algorithm

# Load the configuration data from the JSON file
with open("data/input/config.json") as f:
    config_data = json.load(f)
    # Create a modified copy of config_data with "translate_to_bits" value switched
    config_data_bits = {k: (not v) if k == "translate_to_bits" else v for k, v in config_data.items()}

# Define a test using mark.parametrize to test different target passwords
test_passwords = random.choices(config_data["target_passwords"],k=3)
@pytest.mark.parametrize("password", test_passwords)
@pytest.mark.parametrize("config_data", (config_data, config_data_bits))
# Define the test for the algorithm
def test_genetic_algorithm(password, config_data):
    generation, best_solution, best_fitness_values = genetic_algorithm(password, config_data["parameters"]["N"])
    assert isinstance(generation, int)
    assert isinstance(best_solution, str)
    assert isinstance(best_fitness_values, list)
    assert len(best_fitness_values) == generation + 1
    assert best_solution == password