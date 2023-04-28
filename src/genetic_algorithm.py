import json
import os

import matplotlib.pyplot as plt

from src.components import (evolve_population, generate_initial_population,
                            get_fitness)
from src.config import config_data
from src.mutation_rate import MutationRate
from src.utils import binary_to_char

mutation_rate_manager = MutationRate(config_data["parameters"]["mutation_rate_reset_value"])

def genetic_algorithm(target_password, N):
    """
    Runs a genetic algorithm to evolve a population of candidate solutions and return the best solution.

    Parameters:
    target_password (str): the target password to be guessed
    N (int): the size of the initial population of candidate solutions

    Returns:
    tuple: (generation, best_solution, best_fitness_values) where
            - generation (int): the number of generations required to find the best solution
            - best_solution (str): the best candidate solution found
            - best_fitness_values (list): the list of the best fitness values found at each generation

    """
    show_plot = config_data["show_plot"]
    # Use a genetic algorithm to evolve the population of candidate solutions
    population = generate_initial_population(N, len(target_password))

    while all(fitness == 0 for fitness in [get_fitness(creature, target_password) for creature in population]):
        population = generate_initial_population(N, len(target_password))
    
    generation = 0
    best_results = []

    # Set up the plot if visualization is enabled
    if show_plot:
        fig, ax = plt.subplots()
        line, = ax.plot([], [])
        ax.set_title(f"Best fitness value at every generation (N={N})")
        ax.set_xlabel("Generation")
        ax.set_ylabel("Fitness")
        text = ax.text(0.95, 0.05, f"Mutation rate={mutation_rate_manager.current_rate}", transform=ax.transAxes,
                       fontsize=10, ha='right', va='bottom')
        fig.canvas.mpl_connect('key_press_event', lambda event: on_key_press(event, text))
    
    results = {
        "generation": 0,
        "best_results": [],
    }

    while True:
        # Evaluate the fitness of the population
        fitness_scores = [get_fitness(creature, target_password) for creature in population]
        best_fitness = max(fitness_scores)
        best_solution = population[fitness_scores.index(best_fitness)]
        print(f"Generation {generation}: {best_solution} ({round(best_fitness,3)}/1.000)")
        best_results.append({"generation": generation, "solution": best_solution, "fitness": best_fitness})
        # Check if we have found the target solution
        if best_solution == target_password:
            print(f"Solution found after {generation} generations: {best_solution}")
            if config_data["translate_to_bits"]:
                print(f"Decyphered: {binary_to_char(best_solution)}")
            results = {"generation": generation, "best_results": best_results}
            save_results(results, config_data, "data/output/results.json")
            return generation, best_solution, [result["fitness"] for result in best_results]
        # Create a new generation of candidate solutions
        population = evolve_population(population, mutation_rate_manager.current_rate, target_password)
        generation += 1

        # Update and plot the best fitness value at every generation
        if show_plot:
            plot_fitness_values(line = line,
                                best_fitness_values = [result["fitness"] for result in best_results],
                                generation = generation)

def save_results(results, config_data, output_file):
    """
    Save the results and the configuration data to a JSON file.

    Parameters:
    results (dict): the results of the genetic algorithm
    config_data (dict): the configuration data used in the genetic algorithm
    output_file (str): the path of the output file

    """
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, "w") as f:
        json.dump({"results": results, "config_data": config_data}, f, indent=4)

def plot_fitness_values(line, best_fitness_values, generation):
    """
    Plots the best fitness value at every generation.

    Parameters:
    line (Line2D): the line to be updated
    best_fitness_values (list): the list of the best fitness values found at each generation
    generation (int): the current generation

    """
    # Update the data of the line with the new best fitness values
    line.set_data(range(generation), best_fitness_values)
    # Recalculates axes limits and scales the view to fit the data
    plt.gca().relim()
    plt.gca().autoscale_view()
    # Suspends the execution of the current thread to update plot 
    plt.pause(0.001)

def on_key_press(event, text):
    """
    Changes the mutation rate when a key is pressed.

    Parameters:
    event: the key press event
    text (Text): the text object to be updated

    """
    if event.key == '+':
        mutation_rate_manager.increase()
    elif event.key == '-':
        mutation_rate_manager.decrease()
    elif event.key == 'r':
        mutation_rate_manager.reset()

    text.set_text(f"Mutation rate={mutation_rate_manager.current_rate}")
    print(f"New mutation rate: {mutation_rate_manager.current_rate}")