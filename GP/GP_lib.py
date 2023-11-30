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
    return new_variable


def generate_operator():
    return Node(random.choice(['+', '-', '*', '/']))


def generate_number(options=None):
    def_options = ['int', 'float']
    if options != None:
        def_options = options
    option = random.choice(def_options)

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
    return Node('while ')


def generate_block(max_depth):
    return generate_program(max_depth - 1,[
        'new_variable',
        'output_statement',
        'if_statement',
        'loop'
        ])


def generate_logical_value():
    return Node(random.choice(['true', 'false']))


def generate_condition(max_depth):
    options = ['number', 'constant', 'comparison_operator', 'logical_operator']

    left_value = generate_program(max_depth - 1, options)
    right_value = generate_program(max_depth - 1, options)
    logical_operator = generate_logical_operator()

    return Node(logical_operator.value, [left_value, right_value])


def generate_if_statement():
    return Node('if')


def generate_program(max_depth, options=None):
    if max_depth <= 0:
        node = generate_number_or_used_values()
        # node.children = [
        #     generate_number_or_used_values()
        # ]
        return node
    #
    # if max_depth == 1:
    #     node = generate_output_statement()
    #     node.children = [
    #         generate_number_or_used_values()
    #     ]
    #     return node

    def_options = [
        'new_variable',
        #'operator',
        #'number',
        #'comparison_operator',
        #'logical_operator',
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
        node = Node(generate_new_variable())
        node.children = [
            generate_program(max_depth - 1, ['assignment',])
        ]
        return node
    elif value == 'number':
        return generate_number()
    elif value == 'comparison_operator':
        node = generate_comparison_operator()
        node.children = [
            generate_program(max_depth - 1, ['generate_number_or_used_values', 'comparison_operator']),
            generate_program(max_depth - 1, ['generate_number_or_used_values', 'comparison_operator'])
        ]
        return node
    elif value == 'generate_number_or_used_values':
        return generate_number_or_used_values()
    elif value == 'logical_operator':
        node = generate_logical_operator()
        node.children = [
            generate_program(max_depth - 1, ['generate_logical_value', 'comparison_operator']),
            generate_program(max_depth - 1, ['generate_logical_value', 'comparison_operator'])
        ]
        return node
    elif value == 'assignment':
        node = generate_assignment()
        node.children = [
            generate_program(max_depth - 1, ['generate_number_or_used_values', 'comparison_operator', 'operator', 'generate_logical_value'])
        ]
        return node
    elif value == 'output_statement':
        node = generate_output_statement()
        node.children = [
            generate_program(max_depth - 1, ['generate_number_or_used_values', 'comparison_operator', 'operator', 'generate_logical_value'])
        ]
        return node
    elif value == 'if_statement':
        node = generate_if_statement()
        node.children = [
                         generate_program(max_depth, ['comparison_operator']),
                         generate_block(max_depth - 1)
                         ]
        return node
    elif value == 'loop':
        node = generate_loop()
        node.children = [
                         generate_program(max_depth, ['comparison_operator']),
                         generate_block(max_depth - 1)
                         ]
        return node
    elif value == 'generate_number_for_loop':
        return generate_number(['int'])


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

def mutate(tree, max_depth):
    mutated_program = copy.deepcopy(tree)

    if len(mutated_program.children) == 0:
        return mutated_program
    node_to_mutate = random.choice(mutated_program.children)


    new_subtree = generate_program(max_depth)

    if isinstance(node_to_mutate.value, type(new_subtree.value)):
        node_to_mutate.value = new_subtree.value
        node_to_mutate.children = new_subtree.children

    return mutated_program


def tournament_selection(population, k):
    selected = []
    for _ in range(len(population)):
        tournament = random.sample(population, k)
        # winner = min(tournament, key=lambda program: adaptation_function(program, input_data))
        #tmp
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


def run(input_data, output_data, population_size, max_depth):
    population = [generate_program(max_depth)
                  for _ in range(population_size)]

    # Example evolution loop
    # for generation in range(10):
    #     fitness_scores = [adaptation_function(program, input_data) for program in population]
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
    elif program.value in {'while ', 'if'}:
        print("  " * indent + f"Block: {program.value}")
    else:
        print("  " * indent + f"Value: {program.value}")

    for child in program.children:
        display_all_nodes(child, indent + 1)

# Reurning program in proper format
def return_program(program):
    pass


max_depth = 5
input_data = np.linspace(-1, 1, 100).reshape(-1, 1)
output_data = 2 * input_data + np.sin(5 * input_data) + np.random.normal(0, 0.1, input_data.shape)

population_size = 1

population = run(input_data, output_data, population_size, max_depth - 1)
# best_program = min(population, key=lambda program: adaptation_function(output_data, adaptation_function(program, input_data)))
best_program = population[0]

serialize_program(best_program, 'serialized_program_regression.pkl')
deserialized_program = deserialize_program('serialized_program_regression.pkl')
display_all_nodes(deserialized_program)

# for i in population:
#     display_all_nodes(deserialized_program)
#     print('------------------------------------')
