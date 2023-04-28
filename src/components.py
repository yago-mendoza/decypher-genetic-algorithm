import random

from src.config import config_data


def get_fitness(creature, target_password):
    """Calculates the fitness of a candidate solution.

    Args:
        creature (str): The candidate solution to evaluate.
        target_password (str): The target password to match against.

    Returns:
        float: The fitness score of the candidate solution, ranging from 0 (no match) to 1 (exact match).
    """
    # Calculate the fitness of a candidate solution
    return sum(target_password[i] == creature[i] for i in range(len(target_password)))/len(target_password)

def evolve_population(population, mutation_rate, target_password):
    """Evolves a population of candidate solutions to the next generation.

    Args:
        population (list of str): The current population of candidate solutions.
        mutation_rate (float): The probability of a mutation occurring in a given candidate solution.
        target_password (str): The target password to match against.

    Returns:
        list of str: The new population of candidate solutions.
    """
    parents_per_child = config_data["parameters"]["parents_per_child"]
    site_specific_mutations = config_data["parameters"]["site_specific_mutations"]
    # Create a new generation of candidate solutions by selecting parents and applying 
    new_population = []
    fitness_scores = [get_fitness(creature, target_password) for creature in population]
    for i in range(len(population)):
        # Select parents with probability proportional to their fitness
        parents = random.choices(population, weights=fitness_scores, k=parents_per_child)
        # Apply crossover operator to create a new child
        crossover_points = sorted(random.sample(range(len(target_password)), parents_per_child - 1))
        child_segments = []
        for j in range(parents_per_child):
            if j == 0:
                child_segments.append(parents[0][:crossover_points[j]])
            elif j == parents_per_child - 1:
                child_segments.append(parents[-1][crossover_points[j-1]:])
            else:
                child_segments.append(parents[j][crossover_points[j-1]:crossover_points[j]])
        child = ''.join(child_segments)
        # Apply mutation operator to introduce random variation (changes a single character)
        if random.random() < mutation_rate: 
            if site_specific_mutations:
                # Choose a mutation point that is not healthy (different from target)
                mutation_points = [i for i in range(len(target_password)) if target_password[i] != child[i]]
            if not site_specific_mutations:
                # Choose a random mutation point
                mutation_points = [random.choice(range(len(target_password)))]
            # Apply mutations
            for mutation_point in mutation_points:
                child = child[:mutation_point] + random.choice(config_data["charset"]) + child[mutation_point+1:]
        new_population.append(child)
    return new_population

def generate_initial_population(N, target_password_length):
    """Generates an initial population of candidate solutions.
    
    Args:
        N (int): The size of the population to generate.
        target_password_length (int): The length of the target password to match against.

    Returns:
        list of str: The initial population of candidate solutions.
    """
    # Generate the initial population of candidate solutions
    initial_population = []
    for i in range(N):
        # Generate a random string of characters
        candidate_solution = ''.join(random.choice(config_data["charset"]) for _ in range(target_password_length))
        initial_population.append(candidate_solution)
    return initial_population