import random
import numpy as np
import program_variables as PV
import program_evaluator as evaluator
import matplotlib.pyplot as plt

used_variables = set()

class Program:
    def __init__(self):
        self.variables = set()
        self.program = []


class Node:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children or []


def generate_new_variable(variables: set):
    new_variable = 'i' + str(random.randint(1, 99999))
    while new_variable in variables:
        new_variable = 'i' + str(random.randint(1, 99999))
    variables.add(new_variable)
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


def generate_number_or_used_values(variables):
    options = ['int', 'input']
    if len(used_variables) > 0:
        options.append('used_variables')

    option = random.choice(options)
    if option == 'int':
        return Node(str(random.randint(0, 9)))
    elif option == 'input':
        return Node('input')
    elif option == 'used_variables':
        return Node(str(random.choice(list(variables))))


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


def generate_block(max_depth, variables):
    if max_depth <= 2:
        return generate_program(max_depth - 1, variables, [
            'new_variable',
            'output_statement',
        ])
    else:
        return generate_program(max_depth - 1, variables, [
            'new_variable',
            'output_statement',
            'if_statement',
            'loop',
        ])


def generate_logical_value():
    return Node(random.choice(['true', 'false']))


def generate_condition(max_depth, variables):
    options = ['number', 'constant', 'comparison_operator', 'logical_operator']

    left_value = generate_program(max_depth - 1, variables, options)
    right_value = generate_program(max_depth - 1, variables, options)
    logical_operator = generate_logical_operator()

    return Node(logical_operator.value, [left_value, right_value])


def generate_if_statement():
    return Node('if')


def generate_program(max_depth, variables: set, options=None, isMutation=False):
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
        node = Node(generate_new_variable(variables))
        node.children = [
            generate_program(max_depth - 1, variables, ['assignment', ])
        ]
        return node
    elif value == 'number':
        return generate_number()
    elif value == 'comparison_operator':
        node = generate_comparison_operator()
        node.children = [
            generate_program(max_depth - 1, variables, ['generate_number_or_used_values', 'comparison_operator']),
            generate_program(max_depth - 1, variables, ['generate_number_or_used_values', 'comparison_operator'])
        ]
        return node
    elif value == 'generate_number_or_used_values':
        return generate_number_or_used_values(variables)
    elif value == 'logical_operator':
        node = generate_logical_operator()
        node.children = [
            generate_program(max_depth - 1, variables, ['generate_logical_value', 'comparison_operator']),
            generate_program(max_depth - 1, variables, ['generate_logical_value', 'comparison_operator'])
        ]
        return node
    elif value == 'assignment':
        node = generate_assignment()
        node.children = [
            generate_program(max_depth - 1, variables, ['generate_number_or_used_values', 'comparison_operator', 'operator',
                                             'generate_logical_value'])
        ]
        return node
    elif value == 'output_statement':
        node = generate_output_statement()
        node.children = [
            generate_program(max_depth - 1, variables, ['generate_number_or_used_values', 'comparison_operator', 'operator',
                                             'generate_logical_value'])
        ]
        return node
    if value in {'if_statement', 'loop'}:
        node = generate_if_statement() if value == 'if_statement' else generate_loop()
        condition = generate_program(3, variables, ['comparison_operator'])

        if condition is None:
            condition = generate_program(3, variables, ['comparison_operator'])

        body = generate_block(max_depth - 1, variables)

        if body is None:
            body = generate_block(max_depth - 1, variables)

        node.children = [condition, body]
        return node
    elif value == 'generate_number_for_loop':
        return generate_number(['int'])


def serialize_program(program, filename):
    with open(filename, "wt") as file:
        file.write(program)


def deserialize_program(filename):
    with open(filename, 'rb') as file:
        return file.read()


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


def generate_random_statement(variables):
    options = [
        'new_variable',
        'output_statement',
        'if_statement',
        'loop'
    ]
    choice = random.choice(options)
    if choice == 'new_variable':
        return generate_new_variable(variables)
    elif choice == 'output_statement':
        return generate_output_statement()
    elif choice == 'if_statement':
        return generate_if_statement()
    elif choice == 'loop':
        return generate_loop()


def mutate_program(program, max_depth, max_width, mutation_rate, variables):
    if isinstance(program, list):
        for i in range(1, max_width - 1):
            j = random.randint(0, len(program) - 1)
            program[j] = mutate_program(program[j], max_depth - 1, max_width, mutation_rate, variables)
        return program

    if random.randint(0, 100)/100 < mutation_rate:
        return generate_program(random.randint(1, max_depth + 2), variables, None, True)
    elif program is not None:
        for child in program.children:
            if max_depth >= 0:
                mutate_program(child, max_depth - 1, max_width, mutation_rate, variables)
    return program


def crossover(parent1: Program, parent2: Program):
    parent1_nodes = [node for node in parent1.program]
    parent2_nodes = [node for node in parent2.program]

    cross_point1 = random.randint(0, len(parent1_nodes) - 1)
    cross_point2 = random.randint(0, len(parent2_nodes) - 1)

    parent1.program[cross_point1], parent2.program[cross_point2] = parent2_nodes[cross_point2], parent1_nodes[cross_point1]

    return parent1, parent2


def mean_squared_error(output, target):
    return np.mean((output - target) ** 2)


def fitness(program, input_data, target_output):
    ftn = []
    try:
        for i in range(len(target_output)):
            if len(input_data) > i:
                inp = input_data[i]
            else:
                inp = []
            serialized_program = return_program(program)
            serialize_program(serialized_program, './program.txt')
            evaluator.run_generated(inp)
            result = evaluator.get_output()
            res_len = len(result)
            ex_len = len(target_output[i])
            if res_len < ex_len:
                ftn.append(res_len / ex_len)
            else:
                ftn.append(ex_len / res_len)
    except:
        serialized_program = return_program(program)
        with open('error.txt', "a") as file:
            file.write("\n_________________________________________________\n")
            file.write(serialized_program)
        return -1

    return np.mean(ftn)


def return_program(program):
    output = ""
    if isinstance(program, Program):
        output += return_program(program.program)
    elif isinstance(program, list):
        for i, part in enumerate(program):
            output += return_part(part)
            output += "\n"
    else:
        output += return_part(program)
        output += "\n"
    return output


def generate_program_base(max_depth, max_width):
    width = random.randint(1, max_width)
    pp = Program()
    pp.program = [generate_program(max_depth, pp.variables) for _ in range(width)]
    return pp


def add_to_programs(program, fitness, generation):
    serialized_program = return_program(program)
    with open('best_by_generations.txt', "a") as file:
        file.write("\n_________________________________________________\n")
        file.write(f"Generation: {generation}\n")
        file.write(f"Fitness: {fitness}\n\n")
        file.write(serialized_program)

def process_data(data):
    output = []
    for line in data:
        output.append(line.split())
    return [[int(x) for x in z] for z in output]

def run(input_data, output_data, population_size, max_depth, max_width, generations):
    avg_fitnesses = []
    max_fitnesses = []
    output_data = process_data(output_data)
    input_data = process_data(input_data)
    serialize_program("", './program.txt')
    with open('best_by_generations.txt', "w") as file:
        file.write("")
    population = []
    for _ in range(population_size):
        population.append(generate_program_base(max_depth, max_width))

    max_fitness = -1
    best_program = None

    for generation in range(generations):
        for idx, prog in enumerate(population):
            fitness_score = fitness(prog, input_data, output_data)
            if fitness_score < 0:
                used_variables.clear()
                population[idx] = generate_program_base(max_depth, max_width)
            elif fitness_score > max_fitness:
                max_fitness = fitness_score
                best_program = prog

        fitness_scores = [fitness(prog, input_data, output_data) for prog in population]

        max_fitness_index = fitness_scores.index(max(fitness_scores))

        add_to_programs(population[max_fitness_index], fitness_scores[max_fitness_index], generation)

        avg_fitness = sum(fitness_scores) / len(fitness_scores)

        print(f'______________________{generation}_____________________________')
        print(f'Max Fitness: {fitness_scores[max_fitness_index]}')
        print(f'Avg Fitness: {avg_fitness}')
        avg_fitnesses.append(avg_fitness)
        max_fitnesses.append(fitness_scores[max_fitness_index])
        plt.axis([0, generation + 1, -1.0, 1.0])
        plt.plot(range(0, generation + 1), avg_fitnesses, label="Avg Fitness")
        plt.plot(range(0, generation + 1), max_fitnesses, label="Max Fitness")
        plt.legend()
        plt.pause(0.05)

        if fitness_scores[max_fitness_index] >= 1.0:
            print("__________!!! SOLVED !!!__________")
            print(f"______________GENERATION: {generation}_________________")
            serialized_program = return_program(population[max_fitness_index])
            print('Best program:')
            print('___________________________________________')
            print(serialized_program)
            serialize_program(serialized_program, './best_program.txt')
            return population

        max_fitness_program = population[max_fitness_index]
        max_fitness_program.program = mutate_program(max_fitness_program.program, PV.MAX_DEPTH - 1, PV.MAX_WIDTH,
                                                     PV.MUTATION_RATE, max_fitness_program.variables)
        population[max_fitness_index] = max_fitness_program

        parents = random.sample(population, 2)
        children = crossover(*parents)

        population.remove(parents[0])
        population.remove(parents[1])
        population.extend(children)

    print("__________!!! FINISHED !!!__________")
    print(f'Best Fitness: {max_fitness}')
    serialized_program = return_program(best_program)
    print('__________________Best program_________________________')
    print(serialized_program)
    serialize_program(serialized_program, './best_program.txt')

    return population