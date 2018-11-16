from syntacticdata import SyntacticData
from algorithm import Algorithm

if __name__ == '__main__':
    sd = SyntacticData(num_machines=4, num_jobs=10)
    sd.create_predefine_process_time_matrix()
    # sd.generate_process_time_matrix()

    algorithm = Algorithm(sd.process_time_df)
    algorithm.manager()

    algorithm.find_the_optimal_schedule_with_brute_force(sd.process_time_df)
    print('optimal order :', algorithm.best_order)
