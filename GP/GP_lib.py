import random
import pickle
import numpy as np
import program_variables as PV

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
    def_options = ['int']
    if options != None:
        def_options = options
    option = random.choice(def_options)

    if option == 'int':
        return Node(str(random.randint(0, 9)))

def generate_number_or_used_values():
    options = ['int', 'input']
    if len(used_variables) > 0:
        options.append('used_variables')

    option = random.choice(options)
    if option == 'int':
        return Node(str(random.randint(0, 9)))
    elif option == 'input':
        return Node('input')
    elif option == 'used_variables':
        return Node(str(random.choice(list(used_variables))))


def generate_comparison_operator():
    return Node(random.choice(['==', '!=', '<', '>', '<=', '>=']))


def generate_logical_operator():
    return Node(random.choice(['&&', '||']))


def generate_assignment():
    return Node('=')


def generate_output_statement():
    return Node('output')


def generate_loop():
    return Node('while ')


def generate_block(max_depth):
    if max_depth <= 2:
        return generate_program(max_depth - 1, [
            'new_variable',
            'output_statement',
        ])
    else:
        return generate_program(max_depth - 1, [
            'new_variable',
            'output_statement',
            'if_statement',
            'loop',
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


def generate_program(max_depth, options=None, isMutation=False):
    if max_depth <= 3:
        def_options = [
            'new_variable',
            'output_statement'
        ]
    else:
        def_options = [
            'new_variable',
            'output_statement',
            'if_statement',
            'loop'
        ]

    if options is not None:
        def_options = options

    if max_depth == 0 or (max_depth == 1 and isMutation is True):
        return

    if max_depth == 1:
        def_options = ['generate_number_or_used_values']

    if max_depth == 2:
        def_options = list(set(def_options) - {'new_variable', 'loop', 'if_statement'})

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
            generate_program(max_depth - 1, ['assignment', ])
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
            generate_program(max_depth - 1, ['generate_number_or_used_values', 'comparison_operator', 'operator',
                                             'generate_logical_value'])
        ]
        return node
    elif value == 'output_statement':
        node = generate_output_statement()
        node.children = [
            generate_program(max_depth - 1, ['generate_number_or_used_values', 'comparison_operator', 'operator',
                                             'generate_logical_value'])
        ]
        return node
    if value in {'if_statement', 'loop'}:
        node = generate_if_statement() if value == 'if_statement' else generate_loop()
        condition = generate_program(max_depth, ['comparison_operator'])

        # If condition is None, then we don't have a valid 'if' or 'while' statement. Need to regenerate condition.
        if condition is None:
            condition = generate_program(max_depth, ['comparison_operator'])

        body = generate_block(max_depth - 1)

        # If body is None, then our 'if' or 'while' doesn't have a proper body. Need to regenerate body.
        if body is None:
            body = generate_block(max_depth - 1)

        node.children = [condition, body]
        return node
    elif value == 'generate_number_for_loop':
        return generate_number(['int'])


def generate_code(program):
    if isinstance(program.value, str):
        return program.value + " " + " ".join(generate_code(child) for child in program.children)
    else:
        return program.value


def serialize_program(program, filename):
    with open(filename, "wt") as file:
        file.write(program)


def deserialize_program(filename):
    with open(filename, 'rb') as file:
        return pickle.load(file)


def return_part(program):
    if program is None:
        return ''

    if program.value == 'output':
        if program.children:
            return f'output {return_part(program.children[0])};'
        else:
            return 'output;'
    elif program.value == '=':
        variable_name = return_part(program.children[0])
        variable_value = return_part(program.children[1]) if len(program.children) == 2 else ''
        return f'{variable_name} = {variable_value};'
    elif program.value in {'&&', '||', '<', '<=', '==', '!=', '>', '>='}:
        if len(program.children) == 2:
            left_operand = return_part(program.children[0])
            right_operand = return_part(program.children[1])
            return f'{left_operand} {program.value} {right_operand}'
    elif program.value in {'+', '-', '*', '/'}:
        if len(program.children) == 2:
            left_operand = return_part(program.children[0])
            right_operand = return_part(program.children[1])
            return f'{left_operand} {program.value} {right_operand}'
    elif program.value == 'while ':
        if len(program.children) == 2:
            condition = return_part(program.children[0])
            body = return_part(program.children[1])
            return f'while {condition} {{ {body} }}'
    elif program.value == 'if':
        if len(program.children) == 2:
            condition = return_part(program.children[0])
            body = return_part(program.children[1])
            return f'if {condition} {{ {body} }}'
    elif program.value in {'true', 'false', 'input'}:
        return program.value
    elif program.value.startswith('i'):
        if program.children:
            value = return_part(program.children[0])
            result = value[:-4]
            return f'{program.value} = {result};'
        else:
            return f'{program.value}'
    else:
        children_str = " ".join(return_part(child) for child in program.children if child is not None)
        result = f'{program.value} {children_str}'.strip()
        return f'({result})' if program.children else result



def generate_random_statement():
    options = [
        'new_variable',
        'output_statement',
        'if_statement',
        'loop'
    ]
    choice = random.choice(options)
    if choice == 'new_variable':
        return generate_new_variable()
    elif choice == 'output_statement':
        return generate_output_statement()
    elif choice == 'if_statement':
        return generate_if_statement()
    elif choice == 'loop':
        return generate_loop()

def mutate_program(program, max_depth, max_width, mutation_rate):
    if isinstance(program, list):
        for i in range(1, max_width-1):
            j = random.randint(0, len(program)-1)
            program[j] = mutate_program(program[j], max_depth - 1, max_width, mutation_rate)
        return program

    if random.random() < mutation_rate:
        return generate_program(random.randint(1, max_depth + 2), None, True)
    elif program is not None:
        for child in program.children:
            if max_depth >= 0:
                mutate_program(child, max_depth - 1, max_width, mutation_rate)
    return program


def crossover_programs(program1, program2):
    # Flatten the program trees into lists for easier manipulation
    flat_program1 = np.array(program1.flatten())
    flat_program2 = np.array(program2.flatten())

    def find_crossover_node(program):
        for i in range(len(program)):
            node = program[i]
            # Ensure crossover point is within grammar restrictions (avoid breaking the structure)
            if isinstance(node, Node) and node.value in ['print', 'input', 'output', 'if', 'while', '=']:
                return i

    # pick a node from each tree
    cross_node1 = find_crossover_node(flat_program1)
    cross_node2 = find_crossover_node(flat_program2)

    # Perform the crossover
    temp = flat_program1[cross_node1]
    flat_program1[cross_node1] = flat_program2[cross_node2]
    flat_program2[cross_node2] = temp

    # Reshape the programs back to their tree structure
    program1 = flat_program1.reshape(program1.structure())
    program2 = flat_program2.reshape(program2.structure())

    return program1, program2


def flatten_tree(tree):
    for node in tree:
        if isinstance(node, list):
            yield from flatten_tree(node)
        else:
            yield node


def get_parent(tree, target_node):
    for node in tree:
        if isinstance(node, list):
            if target_node in node:
                return node
            else:
                parent = get_parent(node, target_node)
                if parent is not None:
                    return parent
    return None

def mean_squared_error(output, target):
    return np.mean((output - target) ** 2)

def fitness(program, input_data, target_output):
    return random.randint(0,10)


def return_program(program):
    output = ""
    if isinstance(program, list):
        for i, part in enumerate(program):
            output += return_part(part)
            output += "\n"
    else:
        output += return_part(program)
        output += "\n"
    return output

def generate_program_base(max_depth, max_width):
    width = random.randint(1, max_width)
    return [generate_program(max_depth) for _ in range(width)]

def run(input_data, output_data, population_size, max_depth, max_width, generations):
    population = [generate_program_base(max_depth, max_width) for _ in range(population_size)]

    for i in range(generations):
        best_program_index = 0

        # Find the best program in the population
        for j in range(1, population_size):
            if fitness(population[j], input_data, output_data) > fitness(population[best_program_index], input_data,
                                                                         output_data):
                best_program_index = j

        best_program = population[best_program_index]

        mutated_best_program = mutate_program(best_program, PV.MAX_DEPTH - 1, PV.MAX_WIDTH, 0.5)
        population[best_program_index] = mutated_best_program

        print(f'______________________{i}_____________________________')
        for j, program in enumerate(population):
            serialized_program = return_program(program)
            print(f'Individual {j + 1}:\n{serialized_program}')
            print('------------------------------------')

    return population


input_data = np.linspace(-1, 1, 100).reshape(-1, 1)
output_data = 2 * input_data + np.sin(5 * input_data) + np.random.normal(0, 0.1, input_data.shape)

population = run(input_data, output_data, PV.POPULATION_SIZE, PV.MAX_DEPTH - 1, PV.MAX_WIDTH, PV.GENERATIONS)
best_program = population[0]

for i, program in enumerate(population):
    serialized_program = return_program(program)
    print(f'Individual {i + 1}:\n{serialized_program}')
    print('------------------------------------')

serialize_program(return_program(best_program), '../Language/text.txt')
