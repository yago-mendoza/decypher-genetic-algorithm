import json
import random

import pytest

from src.components import evolve_population, generate_initial_population

# Load the configuration data from the JSON file
with open("data/input/config.json") as f:
    config_data = json.load(f)
# Select 10 random passwords for testing
test_passwords = random.choices(config_data["target_passwords"],k=10)
# Define a list of different population sizes for testing
population_sizes = [100, 500, 1000]

# Test the generate_initial_population function (crosses parameters)
@pytest.mark.parametrize("password", test_passwords)
@pytest.mark.parametrize("N", population_sizes)
def test_generate_initial_population(N, password):
    password_length = len(password)
    initial_population = generate_initial_population(N, password_length)
    # Check if the size of the population is correct
    assert len(initial_population) == N
    # Check if the length of each candidate solution is correct
    assert all(len(candidate_solution) == password_length for candidate_solution in initial_population)

# Test the evolve_population function (crosses parameters)
@pytest.mark.parametrize("password", test_passwords)
@pytest.mark.parametrize("N", population_sizes)
def test_evolve_population(N, password):
    password_length = len(password)
    population = generate_initial_population(N, password_length)
    mutation_rate = 0.01
    new_population = evolve_population(population, mutation_rate, password)
    # Check if the size of the new population is correct
    assert len(new_population) == len(population)
    # Check if the length of each candidate solution in the new population is correct
    assert all(len(candidate_solution) == len(password) for candidate_solution in new_population)