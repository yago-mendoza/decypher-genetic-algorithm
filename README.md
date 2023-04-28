# decypher-genetic-algorithm
This code implements a genetic algorithm to find a target password using evolutionary principles, with configuration settings loaded from a JSON file and options for visualization and mutation rate control.

## Requirements

To run this project, you will need:

* Python 3.7 or higher
* The following Python packages: 'matplotlib', 'pytest'

## Installation

1. Clone or donwload the repository to your local machine.
2. Install the required packages mentioned previously, if not already installed

## Usage

### 1. Setting parameters

Before executing the algorithm, you can modify the configuration settings of the password guesser by editing the `config.json` file in the `data/input directory`. The following parameters can be changed:

* `translate_to_bits`: this parameter enables the parsing of the target password into its binary expression, providing an optimized approach for the genetic algorithm application. When activated, the program will only test binary values, while if deactivated, it will consider a wide ASCII spectrum. By default, this parameter is set to `true`.
* `show_plot`: enabling this parameter to `true` will activate a real-time plot of the fitness value being optimized by the algorithm, which provides a useful visualization but may also result in slower execution, particularly during the running of Pytest scripts.
* `target_index`: this index is used to select one of the passwords stored in `target_passwords`. The variable `target_passwords` constitutes a sample of possible passwords, and can be modified without compromising the proper functioning of the code.

Concerning the algorithm parameters, the following settings can be adjusted.

* `N`: size of the population
* `mutation_rate_reset_value`: default value for the mutation rate
* `mutation_rate_increase_factor`: default factor for the increase of the mutation rate
* `mutation_rate_decrease_factor`: default factor for the decrease of the mutation rate
* `parents_per_child`: number of parents combined to create a child
* `site_specific_mutations`: used to focus mutations on characters that do not match the ones in the target. This greatly improves the algorithm's performance, especially in later generations. However, it is recommended to keep this parameter set to `false`, as it deviates from the core concept of a genetic algorithm broader application.

### 2. Running the algorithm

To run the algorithm, simply run the start.py script with the following command:

```python
python start.py
```

A _genetic algorithm_ is a type of search algorithm that mimics the process of natural selection, where the fittest individuals are more likely to survive and produce offspring. When the `start.py` script is executed, the algorithm begins with an initial population of random solutions, which are then evaluated based on a fitness function. Iteratively, the fittest individuals are selected to "breed" and produce new offspring, which inherit traits from their parents, until a satisfactory solution is found.

In addition, you have the option to **dynamically adjust the mutation rate parameter** during execution using the `+` and `-` keys. This feature provides a clear and intuitive way to study the effects of mutations and can be particularly useful for optimizing the solution in real-time. Furthermore, you can reset the mutation rate to its default value by pressing the `r` key.

At every execution, the result of every generation will be stored at the `results.json` file in the `data/output` directory.

## Testing

The project includes a suite of tests that can be run using the following command:

```python
pytest tests/test_name.py
```

The tests cover the functionality of the `generate_initial_population` and `evolve_population` functions, as well as the overall functionality of the `genetic_algorithm` script.

## Contributing

If you find a bug or have a suggestion for improvement, please open an issue or submit a pull request. Contributions are always welcome!

## License

Distributed under the MIT License. See [MIT](https://choosealicense.com/licenses/mit/) for more information.

## Contact Me

If you need to contact me for any reason, feel free to reach out to me at yagomendoza.dev@gmail.com.
I will do my best to respond to your message as soon as possible.
