import pandas as pd
import numpy as np


class SyntacticData(object):

    def __init__(self, num_machines, num_jobs):
        self.num_machines = num_machines
        self.num_jobs = num_jobs
        self.process_time_df = None

    def create_predefine_process_time_matrix(self):
        process_time = {1: [5, 9, 8, 10, 1],
                        2: [9, 3, 10, 1, 8],
                        3: [9, 4, 5, 8, 6],
                        4: [4, 8, 8, 7, 2]}
        self.process_time_df = pd.DataFrame.from_dict(process_time, orient='index',
                                                  columns=range(1, (max(process_time.keys()) + 2)))

    def generate_process_time_matrix(self):
        self.process_time_df = pd.DataFrame(np.random.randint(0, 100, size=(self.num_jobs, self.num_machines)),
                                            index=range(0, self.num_jobs),
                                            columns=range(0, self.num_machines))

