import pandas as pd
import numpy as np


class Algorithm(object):

    def __init__(self, process_time_df):
        self.process_time_df = process_time_df
        self.total_completion_time = None
        self.best_order = []

    def order_jobs_in_descending_order_of_total_completion_time(self):
        total_completion_time = self.process_time_df.sum(axis=1)
        total_completion_time.sort_values(ascending=False, inplace=True)
        return total_completion_time

    def initiate_the_algorithm(self, first_two_jobs):
        '''
        Initiate the algorithm by checking the first two jobs from the descending order list.
        create two permutations and check which one of them is the best.
        :param first_two_jobs:
        :return: the best permutation
        '''
        best_order = []
        initial_pair_jobs_perm_1 = first_two_jobs
        initial_pair_jobs_perm_2 = [initial_pair_jobs_perm_1[1], initial_pair_jobs_perm_1[0]]
        c_1 = self.compute_completion_time(initial_pair_jobs_perm_1)
        c_2 = self.compute_completion_time(initial_pair_jobs_perm_2)
        if c_1 < c_2:
            best_order.append(initial_pair_jobs_perm_1[0])
            best_order.append(initial_pair_jobs_perm_1[1])
            print(c_1, best_order)
        else:
            best_order.append(initial_pair_jobs_perm_2[0])
            best_order.append(initial_pair_jobs_perm_2[1])
            print(c_2, best_order)
        return best_order

    @staticmethod
    def create_permutations(list_jobs, job):
        '''
        Create permutations od order by placing 'job' in every place in 'list_jobs', without hurting thr original order.
        [3,1] , 2 --> [2,3,1], [3,2,1], [3,1,2]
        :param list_jobs: original permutation
        :param job: the job yo create the permutations.
        :return: list of list (all int)
        '''
        list_permutations = []
        for i in range(0, len(list_jobs) + 1):
            permutation = list_jobs.copy()
            permutation.insert(i, job)
            list_permutations.append(permutation)
        return list_permutations

    def find_the_best_order_by_heuristic(self, process_time_df, total_completion_time):
        n = process_time_df.shape[0]
        i = 3
        while i < (n+1):
            perms = self.create_permutations(self.best_order, total_completion_time.index[i-1].tolist())
            c_max = np.infty
            for order_jobs in perms:
                current_c_max = self.compute_completion_time(order_jobs)
                if current_c_max < c_max:
                    c_max = current_c_max
                    self.best_order = order_jobs
            i += 1
            print(c_max, self.best_order)
        return self.best_order

    def compute_completion_time(self, list_jobs):
        '''
        Compute the maximum completion time of jobs which goes through the m machine
        according to Flow-Shop Sequencing Problem
        :param list_jobs: list of jobs in a specific order, jobs could be [2, n] (int)
        :return: maximum completion time := C_max (float)
        '''
        completion_time = pd.DataFrame(index=list_jobs, columns=self.process_time_df.columns)
        ct_1 = 0
        for machine in completion_time.columns:
            job = completion_time.index[0]
            ct_1 += self.process_time_df.loc[job, machine]
            completion_time.loc[completion_time.index == job, machine] = ct_1
        for job_relative_place in range(1, (completion_time.shape[0])):
            job = completion_time.index[job_relative_place]
            ct = 0
            for machine_relative_place in range(0, completion_time.shape[1]):
                machine = completion_time.columns[machine_relative_place]
                ct_prev_job_same_machine = completion_time.iloc[job_relative_place-1, machine_relative_place]
                pt_current_job = self.process_time_df.loc[self.process_time_df.index == job, machine].values[0]
                ct = pt_current_job + max(ct_prev_job_same_machine, ct)
                completion_time.loc[completion_time.index == job, machine] = ct
        return completion_time.iloc[completion_time.shape[0]-1, completion_time.shape[1]-1]

    def manager(self):
        self.total_completion_time = self.order_jobs_in_descending_order_of_total_completion_time()
        self.best_order = self.initiate_the_algorithm(self.total_completion_time.index[0:2].tolist())
        self.find_the_best_order_by_heuristic(self.process_time_df, self.total_completion_time)