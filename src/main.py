from src.config import config_data
from src.genetic_algorithm import *


def main ():

    # Get the target password and population size from the config file
    TARGET_PASSWORD = config_data["target_passwords"][config_data["target_index"]]
    N = config_data["parameters"]["N"]

    # Run the genetic algorithm with the target password and population size
    genetic_algorithm(TARGET_PASSWORD, N)