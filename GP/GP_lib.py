import random
import copy
import pickle
import numpy as np

class Node:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children or []

def generate_random_program(max_depth, terminal_nodes, function_nodes):
    if max_depth == 0 or (random.random() < terminal_nodes / (terminal_nodes + function_nodes)):
        return Node(random.uniform(-1.0, 1.0))  # Terminal node (constant)

    """Add values from language"""
    value = random.choice(['+', '-', '*', '/'])  # Function node
    children = [generate_random_program(max_depth - 1, terminal_nodes, function_nodes) for _ in range(2)]
    return Node(value, children)

def crossover(parent1, parent2):
    child1 = copy.deepcopy(parent1)
    child2 = copy.deepcopy(parent2)

    # Ensure that both parents have non-empty children
    if not child1.children or not child2.children:
        return child1, child2

    # Swap subtrees
    subtree1 = random.choice(child1.children)
    subtree2 = random.choice(child2.children)

    subtree1_index = child1.children.index(subtree1)
    child1.children[subtree1_index] = subtree2

    subtree2_index = child2.children.index(subtree2)
    child2.children[subtree2_index] = subtree1

    return child1, child2

def mutate(program, max_depth, terminal_nodes, function_nodes):
    mutated_program = copy.deepcopy(program)

    # Ensure that the program has non-empty children
    if not mutated_program.children:
        return mutated_program

    # Randomly choose a node to mutate
    node_to_mutate = random.choice(mutated_program.children)

    # Mutate value or subtree
    if random.random() < 0.5:
        node_to_mutate.value = random.uniform(-1.0, 1.0)
    else:
        subtree_index = mutated_program.children.index(node_to_mutate)
        mutated_program.children[subtree_index] = generate_random_program(
            max_depth - 1, terminal_nodes, function_nodes)

    return mutated_program


def evaluate_program(program, input_data):
    predictions = []

    for input_point in input_data:
        prediction = evaluate_node(program, input_point)
        predictions.append(prediction)

    return predictions

def evaluate_node(node, input_point):
    """Add values from language"""
    if isinstance(node.value, float):
        return node.value  # Terminal node (constant)
    else:
        if node.value == '+':
            return evaluate_node(node.children[0], input_point) + evaluate_node(node.children[1], input_point)
        elif node.value == '-':
            return evaluate_node(node.children[0], input_point) - evaluate_node(node.children[1], input_point)
        elif node.value == '*':
            return evaluate_node(node.children[0], input_point) * evaluate_node(node.children[1], input_point)
        elif node.value == '/':
            denominator = evaluate_node(node.children[1], input_point)
            if denominator != 0:
                return evaluate_node(node.children[0], input_point) / denominator
            else:
                return 0  # Avoid division by zero

def tournament_selection(population, k):
    tournament = random.sample(population, k)
    # return min(tournament, key=lambda program: adaptation_function(output_data, evaluate_program(program, input_data)))
    return tournament[-1]

def serialize_program(program, filename):
    with open(filename, 'wb') as file:
        pickle.dump(program, file)

def deserialize_program(filename):
    with open(filename, 'rb') as file:
        return pickle.load(file)

'''Function for tensting program'''
def adaptation_function(output, pred) -> float:
    pass


def run(input_data, output_data, population_size, max_depth, terminal_nodes, function_nodes):
    # Generate random population
    population = [generate_random_program(max_depth, terminal_nodes, function_nodes) for _ in range(population_size)]
    # Example evolution loop
    for generation in range(30):
        # Evaluate fitness
        predictions = [evaluate_program(program, input_data) for program in population]
        fitness_scores = [adaptation_function(output_data, prediction) for prediction in predictions]

        parents = [tournament_selection(population, 2) for _ in range(population_size)]

        offspring = []
        for i in range(0, population_size, 2):
            child1, child2 = crossover(parents[i], parents[i + 1])
            offspring.extend([mutate(child1, max_depth, terminal_nodes, function_nodes),
                             mutate(child2, max_depth, terminal_nodes, function_nodes)])

        # Replace old population with offspring
        population = offspring
    return population

'''
Displaying the output tree in a transparent way
'''
def printProgram(program):
    output = list()
    if len(output) > 0:
        printChildren(program, output)
    print(output)

def printChildren(program, output):
    if len(program.children) > 1:
        output.append('(')
        if len(program.children[0].children) > 0:
            printChildren(program.children[0])
        else:
            output.append(program.children[0].value)

        output.append(program.value)

        if len(program.children[1].children) > 0:
            printChildren(program.children[1])
        else:
            output.append(program.children[1].value)
        output.append(')')
    else:
        output.append(program.value)


max_depth = 5
terminal_nodes = 2
function_nodes = 2
input_data = np.linspace(-1, 1, 100).reshape(-1, 1)
output_data = 2 * input_data + np.sin(5 * input_data) + np.random.normal(0, 0.1, input_data.shape)

population_size = 10


population = run(input_data, output_data, population_size, max_depth, terminal_nodes, function_nodes)
# best_program = min(population, key=lambda program: adaptation_function(output_data, evaluate_program(program, input_data)))
# best_program = population[0]

# serialize_program(best_program, 'serialized_program_regression.pkl')
# deserialized_program = deserialize_program('serialized_program_regression.pkl')

for i in population:
    printProgram(i)