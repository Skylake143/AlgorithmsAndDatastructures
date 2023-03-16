import typing
import unittest
import numpy as np
import time
import timeit
import gc

from csp import CSP

##############################################################################################
# Note that in the test cases below, we always use an increasing set of numbers for simplicity
# (e.g., {1,2} or {1,2,3}) but it can be any arbitrary set of numbers, such as {2,1} or 
# {900, 50,1}
##############################################################################################

class TestCSP(unittest.TestCase):
    def test_backtracking_medium(self):
        grid = np.array([
            [1,0,0],
            [3,0,0],
            [0,0,3],
        ])

        solution = np.array([
            [1,3,2],
            [3,2,1],
            [2,1,3],
        ])

        horizontal_groups = []
        for row_idx in range(3):
            groups = [(row_idx, j) for j in range(3)]
            horizontal_groups.append(groups)

        vertical_groups = []
        for col_idx in range(3):
            groups = [(j, col_idx) for j in range(3)]
            vertical_groups.append(groups)


        groups = horizontal_groups + vertical_groups
        constraints = [(sum([1,2,3]),1) for j in range(len(groups))]

        csp = CSP(grid, numbers=set([1,2,3]), groups=groups, constraints=constraints)
        result = csp.start_search_backtracking()

        self.assertTrue(np.all(result == solution))

    def test_greedy_backtracking_medium(self):
        grid = np.array([
            [1,0,0],
            [3,0,0],
            [0,0,3],
        ])

        solution = np.array([
            [1,3,2],
            [3,2,1],
            [2,1,3],
        ])

        horizontal_groups = []
        for row_idx in range(3):
            groups = [(row_idx, j) for j in range(3)]
            horizontal_groups.append(groups)

        vertical_groups = []
        for col_idx in range(3):
            groups = [(j, col_idx) for j in range(3)]
            vertical_groups.append(groups)


        groups = horizontal_groups + vertical_groups
        constraints = [(sum([1,2,3]),1) for j in range(len(groups))]

        csp = CSP(grid, numbers=set([1,2,3]), groups=groups, constraints=constraints)
        result = csp.start_search_greedy_backtracking()

        self.assertTrue(np.all(result == solution))
    
    def test_search_large(self):
        grid = np.array([
            [1,0,0,0],
            [3,0,0,0],
            [0,0,3,0],
            [0,0,4,0]
        ])

        solution = np.array([
            [1,3,2,4],
            [3,4,1,2],
            [4,2,3,1],
            [2,1,4,3]
        ])

        horizontal_groups = []
        for row_idx in range(4):
            groups = [(row_idx, j) for j in range(4)]
            horizontal_groups.append(groups)

        vertical_groups = []
        for col_idx in range(4):
            groups = [(j, col_idx) for j in range(4)]
            vertical_groups.append(groups)

        groups = horizontal_groups + vertical_groups
        constraints = [(sum([1,2,3,4]),1) for j in range(len(groups))]

        csp = CSP(grid, numbers=set([1,2,3,4]), groups=groups, constraints=constraints)
        result = csp.start_search()

        self.assertTrue(np.all(result == solution))

    def test_time_comparison(self):
        #4x4 array
        grid = np.array([
            [1,0,0,0],
            [3,0,0,0],
            [0,0,3,0],
            [0,0,4,0]
        ])

        solution = np.array([
            [1,3,2,4],
            [3,4,1,2],
            [4,2,3,1],
            [2,1,4,3]
        ])

        length_array = 4
        horizontal_groups = []
        for row_idx in range(length_array):
            groups = [(row_idx, j) for j in range(length_array)]
            horizontal_groups.append(groups)

        vertical_groups = []
        for col_idx in range(length_array):
            groups = [(j, col_idx) for j in range(length_array)]
            vertical_groups.append(groups)

        groups = horizontal_groups + vertical_groups
        constraints = [(sum(range(1,length_array+1)),1) for j in range(len(groups))]

        csp = CSP(grid, numbers=set(range(1,length_array+1)), groups=groups, constraints=constraints)

        #EXHAUSTIVE
        #We use monotonic for measuring the time, since it takes a long time
        #disable garbage collector for higher precision
        gc.disable()
        start_time = time.monotonic_ns()
        result_exhaustive = csp.start_search()
        end_time = time.monotonic_ns()
        # re-enable garbage collector
        gc.enable()
        timediff_exhaustive = end_time-start_time
        print('Execution time exhaustive:', timediff_exhaustive/1000000, 'milliseconds')

        #BACKTRACKING

        #TIME.perf_counter_ns()
        #CPU Process time 
        gc.disable()
        start_time = time.perf_counter_ns()   
        result_backtracking = csp.start_search_backtracking()
        end_time = time.perf_counter_ns()
        gc.enable()
        timediff_backtracking = end_time-start_time


        # #SELF-MADE TIMEIT LOGIC
        # total_time_backtracking = 0 
        # repetitions = 100
        # for i in range(repetitions):
        #     gc.disable()
        #     start_time = time.perf_counter_ns()
        #     result_backtracking = csp.start_search_backtracking()
        #     end_time = time.perf_counter_ns()
        #     gc.enable()
        #     timediff_backtracking = end_time-start_time
        #     total_time_backtracking+=timediff_backtracking
        

        # #TIMEIT
        # #since measured time for backtracking is very short we use timit to measure block of code 100 times and calculate 1/100 of it in the end
        # repetitions = 100
        # gc.disable()
        # timediff_backtracking = timeit.timeit(stmt=csp.start_search_backtracking, number=repetitions)
        # gc.enable()u

        # #Get result
        # result_backtracking = csp.start_search_backtracking()
        # #TIMEIT END

        print('Execution time backtracking:', timediff_backtracking/1000000, 'milliseconds')


        #Greedy backtracking 
        gc.disable()
        start_time = time.perf_counter_ns()        
        result_greedy_backtracking = csp.start_search_greedy_backtracking()
        end_time = time.perf_counter_ns()
        gc.disable()
        timediff_greedy_backtracking = end_time-start_time


        # #SELF-MADE TIMEIT LOGIC
        # total_time_greedy_backtracking = 0 
        # repetitions = 1000
        # for i in range(repetitions):
        #     gc.disable()
        #     start_time = time.perf_counter_ns()
        #     result_greedy_backtracking = csp.start_search_greedy_backtracking()
        #     end_time = time.perf_counter_ns()
        #     gc.enable()
        #     timediff_greedy_backtracking = end_time-start_time
        #     total_time_greedy_backtracking+=timediff_greedy_backtracking

        # #TIMEIT
        # #since measured time for backtracking is very short we use timit to measure block of code 10 times and calculate 1/10 of it in the end
        # gc.disable()
        # timediff_greedy_backtracking = timeit.timeit(stmt=csp.start_search_greedy_backtracking, number=repetitions)
        # gc.enable()

        # #Get result
        # result_greedy_backtracking = csp.start_search_greedy_backtracking()
        # #TIMEIT END

        print('Execution time greedy backtracking:', timediff_greedy_backtracking/1000000, 'milliseconds')

        #self.assertTrue(np.all(result_exhaustive == solution))
        self.assertTrue(np.all(result_backtracking == solution))
        self.assertTrue(np.all(result_greedy_backtracking == solution))

    def test_all_numbers_twice(self):
        grid = np.array([
            [1,0,0],
            [3,0,0],
            [0,0,3]
        ])

        solution = np.array([
            [1,1,2],
            [3,1,1],
            [1,2,3]
        ])

        horizontal_groups = []
        for row_idx in range(3):
            groups = [(row_idx, j) for j in range(3)]
            horizontal_groups.append(groups)

        vertical_groups = []
        for col_idx in range(3):
            groups = [(j, col_idx) for j in range(3)]
            vertical_groups.append(groups)

        groups = horizontal_groups + vertical_groups
        constraints = [(sum([1,2,3]),2) for j in range(len(groups))]

        csp = CSP(grid, numbers=set([1,2,3]), groups=groups, constraints=constraints)
        result = csp.start_search_backtracking()

        self.assertTrue(np.all(result == solution))

    def test_sum_constraint_is_0(self):
        grid = np.array([
            [1,0,0],
            [3,0,0],
            [0,0,3]
        ])

        horizontal_groups = []
        for row_idx in range(3):
            groups = [(row_idx, j) for j in range(3)]
            horizontal_groups.append(groups)

        vertical_groups = []
        for col_idx in range(3):
            groups = [(j, col_idx) for j in range(3)]
            vertical_groups.append(groups)

        groups = horizontal_groups + vertical_groups
        constraints = [(0,2) for j in range(len(groups))]

        csp = CSP(grid, numbers=set([1,2,3]), groups=groups, constraints=constraints)
        result = csp.start_search_backtracking()

        self.assertIsNone(result)

    #ERROR TESTs
    #Test group with double group parameters
    def test_search_double_group_error(self):
        horizontal_groups = [[(0,0),(0,0)], [(1,0), (1,1)]]
        vertical_groups = [[(0,0), (1,0)], [(0,1), (1,1)]]
        groups = horizontal_groups + vertical_groups
        # every constraint is of the form (sum, count). so every group must sum to 3 and every number may only occur once per group
        constraints = [(3, 1), (3, 1), (3, 1), (3, 1)]

        valid_grid = np.array([[1,0],
                               [0,0]])

        csp = CSP(valid_grid, numbers=set([1,2]), groups=groups, constraints=constraints)
        result = csp.start_search()

        self.assertIsNone(result)

    #Test group with location out of grid
    #Test group with wrong group parameters
    def test_search_index_out_of_grid(self):
        horizontal_groups = [[(0,0),(0,2)], [(1,0), (1,1)]]
        vertical_groups = [[(0,0), (1,0)], [(0,1), (1,1)]]
        groups = horizontal_groups + vertical_groups
        # every constraint is of the form (sum, count). so every group must sum to 3 and every number may only occur once per group
        constraints = [(3, 1), (3, 1), (3, 1), (3, 1)]

        valid_grid = np.array([[1,0],
                               [0,0]])

        csp = CSP(valid_grid, numbers=set([1,2]), groups=groups, constraints=constraints)
        result = csp.start_search()

        self.assertIsNone(result)

    def test_search_no_solution_no_overwriting(self):
        horizontal_groups = [[(0,0),(0,1)], [(1,0), (1,1)]]
        vertical_groups = [[(0,0), (1,0)], [(0,1), (1,1)]]
        groups = horizontal_groups + vertical_groups
        # every constraint is of the form (sum, count). so every group must sum to 3 and every number may only occur once per group
        constraints = [(3, 1), (3, 1), (3, 1), (3, 1)]

        valid_grid = np.array([[5,0],
                               [0,0]])
        csp = CSP(valid_grid, numbers=set([1,2]), groups=groups, constraints=constraints)
        result = csp.start_search()
        self.assertIsNone(result)