from src.config import config_data


class MutationRate:
    def __init__(self, initial_rate):
        self.initial_rate = initial_rate
        self.current_rate = initial_rate

    def increase(self):
        self.current_rate *= config_data["parameters"]["mutation_rate_increase_factor"]

    def decrease(self):
        self.current_rate /= config_data["parameters"]["mutation_rate_decrease_factor"]

    def reset(self):
        self.current_rate = self.initial_rate


