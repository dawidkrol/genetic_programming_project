import GP.GP_lib as gp
import program_variables as PV
import program_evaluator as evaluator

input_data = []
output_data = [0, 3, 4, 5, 6]

population = gp.run(input_data, output_data, PV.POPULATION_SIZE, PV.MAX_DEPTH - 1, PV.MAX_WIDTH, PV.GENERATIONS)
best_program = population[0]

# for i, program in enumerate(population):
#     serialized_program = gp.return_program(program)
#     print(f'Individual {i + 1}:\n{serialized_program}')
#     gp.serialize_program(serialized_program, 'program.txt')
#     evaluator.run_generated()
#     print(f'\nResult: {evaluator.get_output()}')
#     print('------------------------------------')