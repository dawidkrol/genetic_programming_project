import random
import copy
import pickle
import numpy as np

used_variables = set()

class Node:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children or []

def use_created_variable():
    return Node(random.choice(list(used_variables)))

def generate_new_variable():
    new_variable = 'i' + str(random.randint(1, 99999))
    while new_variable in used_variables:
        new_variable = 'i' + str(random.randint(1, 99999))
    used_variables.add(new_variable)
    return Node(new_variable)


def generate_operator():
    return Node(random.choice(['+', '-', '*', '/']))


def generate_number():
    options = ['int', 'float']
    option = random.choice(options)

    if option == 'int':
        return Node(str(random.randint(0, 9)))
    elif option == 'float':
        return Node(str(random.uniform(-1.0, 1.0)))

def generate_number_or_used_values():
    options = ['int', 'float']
    if len(used_variables) > 0:
        options.append('used_variables')

    option = random.choice(options)
    if option == 'int':
        return Node(str(random.randint(0, 9)))
    elif option == 'float':
        return Node(str(random.uniform(-1.0, 1.0)))
    elif option == 'used_variables':
        return Node(str(random.choice(list(used_variables))))


def generate_comparison_operator():
    return Node(random.choice(['==', '!=', '<', '>', '<=', '>=']))


def generate_logical_operator():
    return Node(random.choice(['&&', '||']))


def generate_assignment():
    return Node('=')


def generate_output_statement():
    return Node('print')


def generate_loop():
    condition = generate_condition(max_depth, terminal_nodes, function_nodes)
    return Node('for a in ')


def generate_block(max_depth, terminal_nodes, function_nodes):
    return generate_program(max_depth - 1, terminal_nodes, function_nodes)


def generate_logical_value():
    return Node(random.choice(['true', 'false']))


def generate_condition(max_depth, terminal_nodes, function_nodes):
    options = ['number', 'constant', 'comparison_operator', 'logical_operator']

    left_value = generate_program(max_depth - 1, terminal_nodes, function_nodes, options)
    right_value = generate_program(max_depth - 1, terminal_nodes, function_nodes, options)
    logical_operator = generate_logical_operator()

    return Node(logical_operator.value, [left_value, right_value])


def generate_if_statement():
    # condition = generate_condition(max_depth, terminal_nodes, function_nodes)
    return Node('if')


def generate_program(max_depth, terminal_nodes, function_nodes, options=None):
    if max_depth == 0:
        return random.choice([generate_number,])()

    def_options = [
        'new_variable',
        'operator',
        'number',
        'comparison_operator',
        'logical_operator',
        'output_statement',
        'if_statement',
        'loop'
        ]

    if options != None:
        def_options = options

    value = random.choice(def_options)

    if value == 'operator':
        node = generate_operator()
        node.children = [
            generate_number(),
            generate_number()
        ]
        return node
    elif value == 'generate_logical_value':
        return generate_logical_value()
    elif value == 'new_variable':
        node = generate_new_variable()
        node.children = [
            generate_program(max_depth, terminal_nodes, function_nodes, ['assignment',])
        ]
        return node
    elif value == 'number':
        return generate_number()
    elif value == 'comparison_operator':
        node = generate_comparison_operator()
        node.children = [
            generate_program(max_depth, terminal_nodes, function_nodes, ['generate_number_or_used_values','comparison_operator']),
            generate_program(max_depth, terminal_nodes, function_nodes, ['generate_number_or_used_values','comparison_operator'])
        ]
        return node
    elif value == 'generate_number_or_used_values':
        return generate_number_or_used_values()
    elif value == 'logical_operator':
        node = generate_logical_operator()
        node.children = [
            generate_program(max_depth, terminal_nodes, function_nodes, ['generate_logical_value', 'comparison_operator']),
            generate_program(max_depth, terminal_nodes, function_nodes, ['generate_logical_value', 'comparison_operator'])
        ]
        return node
    elif value == 'assignment':
        node = generate_assignment()
        node.children = [
            generate_program(max_depth, terminal_nodes, function_nodes, ['generate_number_or_used_values', 'comparison_operator', 'operator', 'generate_logical_value'])
        ]
        return node
    elif value == 'output_statement':
        node = generate_output_statement()
        node.children = [
            generate_program(max_depth, terminal_nodes, function_nodes, ['generate_number_or_used_values', 'comparison_operator', 'operator', 'generate_logical_value'])
        ]
        return node
    elif value == 'if_statement':
        node = generate_if_statement()
        node.children = [
                         generate_program(max_depth, terminal_nodes, function_nodes, ['comparison_operator']),
                         generate_block(max_depth, terminal_nodes, function_nodes)
                         ]
        return node
    elif value == 'loop':
        node = generate_loop()
        node.children = [
                         generate_program(max_depth, terminal_nodes, function_nodes, ['generate_number_or_used_values']),
                         generate_block(max_depth, terminal_nodes, function_nodes)
                         ]
        return node


def generate_code(program):
    if isinstance(program.value, str):
        return program.value + " " + " ".join(generate_code(child) for child in program.children)
    else:
        return program.value


def crossover(parent1, parent2):
    child1 = copy.deepcopy(parent1)
    child2 = copy.deepcopy(parent2)

    if not child1.children or not child2.children:
        return child1, child2

    subtree1 = random.choice(child1.children)

    if not child2.children:
        return child1, child2

    subtree2 = random.choice(child2.children)

    subtree1_index = child1.children.index(subtree1)

    subtree2_index = child2.children.index(subtree2)

    if isinstance(child1.value, type(child2.value)):
        child1.children[subtree1_index].value, child2.children[subtree2_index].value = child2.children[subtree2_index].value, child1.children[subtree1_index].value
        child1.children[subtree1_index].children, child2.children[subtree2_index].children = child2.children[subtree2_index].children, child1.children[subtree1_index].children

    return child1, child2

def mutate(tree, max_depth, terminal_nodes, function_nodes):
    # Create a deep copy of the tree to avoid modifying the original
    mutated_program = copy.deepcopy(tree)

    if len(mutated_program.children) == 0:
        return mutated_program

    # Randomly select a node to mutate
    node_to_mutate = random.choice(mutated_program.children)

    # Generate a new subtree to replace the selected node
    new_subtree = generate_program(max_depth, terminal_nodes, function_nodes)

    # Replace the selected node only if the values are compatible
    if isinstance(node_to_mutate.value, type(new_subtree.value)):
        node_to_mutate.value = new_subtree.value
        node_to_mutate.children = new_subtree.children

    return mutated_program

# def crossover(parent1, parent2):
#     child1 = copy.deepcopy(parent1)
#     child2 = copy.deepcopy(parent2)
#
#     if not child1.children or not child2.children:
#         return child1, child2
#
#     subtree1 = random.choice(child1.children)
#
#     if not child2.children:
#         return child1, child2
#
#     subtree2 = random.choice(child2.children)
#
#     subtree1_index = child1.children.index(subtree1)
#     child1.children[subtree1_index] = subtree2
#
#     subtree2_index = child2.children.index(subtree2)
#     child2.children[subtree2_index] = subtree1
#
#     return child1, child2


# def mutate(program, max_depth, terminal_nodes, function_nodes):
#     mutated_program = copy.deepcopy(program)
#
#     if len(mutated_program.children) == 0:
#         return mutated_program
#
#     node_to_mutate = random.choice(mutated_program.children)
#
#     if random.random() < 0.5:
#         if node_to_mutate.value == 'variable':
#             node_to_mutate.value = generate_number().value
#         elif node_to_mutate.value == 'comparison_operator':
#             node_to_mutate.value = generate_logical_operator().value
#         elif node_to_mutate.value == 'logical_operator':
#             node_to_mutate.value = generate_comparison_operator().value
#     else:
#         subtree_index = mutated_program.children.index(node_to_mutate)
#         if mutated_program.children[subtree_index].value in ['=',]:
#             mutated_program.children[subtree_index].children[0] = generate_number()
#         else:
#             mutated_program.children[subtree_index] = generate_program(max_depth - 1, terminal_nodes, function_nodes)
#
#     return mutated_program


'''Function for tensting program'''

def evaluate_program(program, input_data):
    # Implement your specific evaluation function here
    pass


def tournament_selection(population, k):
    selected = []
    for _ in range(len(population)):
        tournament = random.sample(population, k)
        # winner = min(tournament, key=lambda program: evaluate_program(program, input_data))
        winner = tournament[0]
        selected.append(winner)

    if len(selected) % 2 != 0:
        selected.pop()

    parent_tuples = [(selected[i], selected[i + 1]) for i in range(0, len(selected), 2)]

    return parent_tuples


def serialize_program(program, filename):
    with open(filename, 'wb') as file:
        pickle.dump(program, file)


def deserialize_program(filename):
    with open(filename, 'rb') as file:
        return pickle.load(file)


# '''Function for tensting program'''
def adaptation_function(output, pred) -> float:
    pass


def run(input_data, output_data, population_size, max_depth, terminal_nodes, function_nodes):
    population = [generate_program(max_depth, terminal_nodes, function_nodes)
                  for _ in range(population_size)]

    # Example evolution loop
    # for generation in range(10):
    #     # Evaluate fitness (implement your specific evaluation function)
    #     fitness_scores = [evaluate_program(program, input_data) for program in population]
    #
    #     # Select parents using tournament selection
    #     parents = tournament_selection(population, 2)
    #
    #     # Crossover and mutate
    #     offspring = []
    #     for parent_tuple in parents:
    #         child1, child2 = crossover(parent_tuple[0], parent_tuple[1])
    #         offspring.extend([mutate(child1, max_depth, terminal_nodes, function_nodes),
    #                           mutate(child2, max_depth, terminal_nodes, function_nodes)])
    #
    #     # Replace old population with offspring
    #     population = offspring

    return population


'''
Displaying the output tree in a transparent way
'''


def display_all_nodes(program, indent=0):
    if program == None:
        return
    if program.value in {'&&', '||', '<', '<=', '==', '!=', '>', '>='}:
        print("  " * indent + f"Operator: {program.value}")
    elif program.value in {'true', 'false', '=', '+', '-', '*', '/'}:
        print("  " * indent + f"Operator: {program.value}")
    else:
        print("  " * indent + f"Value: {program.value}")

    for child in program.children:
        display_all_nodes(child, indent + 1)


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
    display_all_nodes(i)
    print('------------------------------------')
