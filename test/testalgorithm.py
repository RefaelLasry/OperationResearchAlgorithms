import unittest
from algorithm import Algorithm
import pandas as pd


class TestAlgorithm(unittest.TestCase):

    def setUp(self):
        process_time = {1: [5, 9, 8, 10, 1],
                        2: [9, 3, 10, 1, 8],
                        3: [9, 4, 5, 8, 6],
                        4: [4, 8, 8, 7, 2]}
        self.process_time_df = pd.DataFrame.from_dict(process_time, orient='index',
                                                      columns=range(1, (max(process_time.keys()) + 2)))
        self.algorithm = Algorithm(self.process_time_df)
        self.total_completion_time = self.algorithm.order_jobs_in_descending_order_of_total_completion_time()
        self.best_order = self.algorithm.initiate_the_algorithm(self.total_completion_time.index[0:2].tolist())

    def tearDown(self):
        self.algorithm = None

    def test_create_permutations(self):
        return_permutations = self.algorithm.create_permutations([3, 1, 2], 4)
        correct_permutations = [[4, 3, 1, 2], [3, 4, 1, 2], [3, 1, 4, 2], [3, 1, 2, 4]]
        self.assertEqual(return_permutations, correct_permutations)

    def test_compute_completion_time(self):
        max_completion_time = self.algorithm.compute_completion_time([3, 1, 2, 4])
        correct_max_completion_time = 58
        self.assertEqual(max_completion_time, correct_max_completion_time)


if __name__ == '__main__':
    unittest.main()