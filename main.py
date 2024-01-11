import GP.GP_lib as gp
import program_variables as PV

with open('./input.txt', 'rb') as file:
    input_data = file.readlines()

with open('./expected_output.txt', 'rb') as file:
    output_data = file.readlines()

population = gp.run(input_data, output_data, PV.POPULATION_SIZE, PV.MAX_DEPTH - 1, PV.MAX_WIDTH, PV.GENERATIONS, PV.MUTATION_RATE)
best_program = population[0]