import GP.GP_lib as gp
import program_variables as PV

input_data = []
output_data = [1, 2, 3, 4, 5, 6, 7, 8]

population = gp.run(input_data, output_data, PV.POPULATION_SIZE, PV.MAX_DEPTH - 1, PV.MAX_WIDTH, PV.GENERATIONS)
best_program = population[0]