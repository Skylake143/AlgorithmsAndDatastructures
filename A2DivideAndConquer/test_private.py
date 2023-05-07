import typing
import unittest
import time 
import timeit
import numpy as np
import gc
import sys

from divconq import IntelDevice


class TestIntelDevice(unittest.TestCase):
    def test_search_solution_ex_grid(self):
            a = np.array([
                [1, 10,14,22,27],
                [11,15,24,28,38],
                [12,23,32,36,42]
            ])

            raw_locations = [f"l{i}" for i in range(12)]
            raw_codes = [str(x) for x in a.reshape(-1)]

            shift = 2
            height=3
            width =5

            # test = IntelDevice(height,width,[],[],shift)
            # encoded_codes=[]
            #         #Iterate through all rows and columns
            # for row in range(height):
            #   for column in range(width):
            # #Add character to location dictionaryx
            #       encoded_codes.append(test.encode_message(str(a[row][column])))
            # print(encoded_codes)

            enc_locations = [
                "1101110 110010", #l0
                "1101110 110011", #l1
                "1101110 110100", #l2
                "1101110 110101", #
                "1101110 110110",
                "1101110 110111",
                "1101110 111000",
                "1101110 111001",
                "1101110 111010", #l8
                "1101110 111011",
                "1101110 111100",
                "1101110 111101",
                "1101110 111110",
                "1101110 111111",
                "1101110 1000000",
                "1101110 1000001"
            ]

            enc_codes = ['110011', '110011 110010', '110011 110110', '110100 110100', '110100 111001', '110011 110011', '110011 110111', '110100 110110', '110100 111010', '110101 111010', '110011 110100', '110100 110101', '110101 110100', '110101 111000', '110110 110100']

            solutions = [
                "1101110 110010", #l0
                "1101110 110011", #l1
                "1101110 110100", #l2
                "1101110 110101",
                "1101110 110110",
                "1101110 110111",
                "1101110 111000",
                "1101110 111001",
                "1101110 111010", #l8
                "1101110 111011",
                "1101110 111100",
                "1101110 111101",
                "1101110 111110",
                "1101110 111111",
                "1101110 1000000",
                "1101110 1000001"
            ]

            ob = IntelDevice(width,height, enc_locations, enc_codes, shift)
            ob.fill_coordinate_to_loc()
            ob.fill_loc_grid()

            # values that occur in the 2d grid
            for vid, v in enumerate(a.reshape(-1)):
                result = ob.start_search(v)
                self.assertEqual(result, solutions[vid])

            
            # values that do not occur should lead to None
            for v in [0,2,18,31,48,60]:
                result = ob.start_search(v)
                self.assertIsNone(result)
    def test_search_solution_ex_grid_linear(self):
            a = np.array([
                [1, 10,14,22,27],
                [11,15,24,28,38],
                [12,23,32,36,42]
            ])

            raw_locations = [f"l{i}" for i in range(12)]
            raw_codes = [str(x) for x in a.reshape(-1)]

            shift = 2
            height=3
            width =5

            # test = IntelDevice(height,width,[],[],shift)
            # encoded_codes=[]
            #         #Iterate through all rows and columns
            # for row in range(height):
            #   for column in range(width):
            # #Add character to location dictionaryx
            #       encoded_codes.append(test.encode_message(str(a[row][column])))
            # print(encoded_codes)

            enc_locations = [
                "1101110 110010", #l0
                "1101110 110011", #l1
                "1101110 110100", #l2
                "1101110 110101", #
                "1101110 110110",
                "1101110 110111",
                "1101110 111000",
                "1101110 111001",
                "1101110 111010", #l8
                "1101110 111011",
                "1101110 111100",
                "1101110 111101",
                "1101110 111110",
                "1101110 111111",
                "1101110 1000000",
                "1101110 1000001"
            ]

            enc_codes = ['110011', '110011 110010', '110011 110110', '110100 110100', '110100 111001', '110011 110011', '110011 110111', '110100 110110', '110100 111010', '110101 111010', '110011 110100', '110100 110101', '110101 110100', '110101 111000', '110110 110100']

            solutions = [
                "1101110 110010", #l0
                "1101110 110011", #l1
                "1101110 110100", #l2
                "1101110 110101",
                "1101110 110110",
                "1101110 110111",
                "1101110 111000",
                "1101110 111001",
                "1101110 111010", #l8
                "1101110 111011",
                "1101110 111100",
                "1101110 111101",
                "1101110 111110",
                "1101110 111111",
                "1101110 1000000",
                "1101110 1000001"
            ]

            ob = IntelDevice(width,height, enc_locations, enc_codes, shift)
            ob.fill_coordinate_to_loc()
            ob.fill_loc_grid()

            # values that occur in the 2d grid
            for vid, v in enumerate(a.reshape(-1)):
                result = ob.start_search_linear(v)
                self.assertEqual(result, solutions[vid])

            
            # values that do not occur should lead to None
            for v in [0,2,18,31,48,60]:
                result = ob.start_search(v)
                self.assertIsNone(result)

    # def test_timer(self):
    #         a = np.array([
    #             [1, 10,14,22,27],
    #             [11,15,24,28,38],
    #             [12,23,32,36,42]
    #         ])



    #         raw_locations = [f"l{i}" for i in range(12)]
    #         raw_codes = [str(x) for x in a.reshape(-1)]

    #         shift = 2
    #         height=3
    #         width =5


    #         test = IntelDevice(height,width,[],[],shift)
    #         encoded_codes=[]
    #                 #Iterate through all rows and columns
    #         for row in range(height):
    #           for column in range(width):
    #         #Add character to location dictionaryx
    #               encoded_codes.append(test.encode_message(str(a[row][column])))
    #         print(encoded_codes)

    #         enc_locations = [
    #             "1101110 110010", #l0
    #             "1101110 110011", #l1
    #             "1101110 110100", #l2
    #             "1101110 110101", #
    #             "1101110 110110",
    #             "1101110 110111",
    #             "1101110 111000",
    #             "1101110 111001",
    #             "1101110 111010", #l8
    #             "1101110 111011",
    #             "1101110 111100",
    #             "1101110 111101",
    #             "1101110 111110",
    #             "1101110 111111",
    #             "1101110 1000000",
    #             "1101110 1000001"
    #         ]

    #         enc_codes = ['110011', '110011 110010', '110011 110110', '110100 110100', '110100 111001', '110011 110011', '110011 110111', '110100 110110', '110100 111010', '110101 111010', '110011 110100', '110100 110101', '110101 110100', '110101 111000', '110110 110100']

    #         solutions = [
    #             "1101110 110010", #l0
    #             "1101110 110011", #l1
    #             "1101110 110100", #l2
    #             "1101110 110101",
    #             "1101110 110110",
    #             "1101110 110111",
    #             "1101110 111000",
    #             "1101110 111001",
    #             "1101110 111010", #l8
    #             "1101110 111011",
    #             "1101110 111100",
    #             "1101110 111101",
    #             "1101110 111110",
    #             "1101110 111111",
    #             "1101110 1000000",
    #             "1101110 1000001"
    #         ]

    #         ob = IntelDevice(width,height, enc_locations, enc_codes, shift)
    #         ob.fill_coordinate_to_loc()
    #         ob.fill_loc_grid()

    #         #SELF-MADE TIMEIT LOGIC
    #         total_time_divconq = 0 
    #         repetitions = 100
    #         result_divconq =0
    #         for i in range(repetitions):
    #             gc.disable()
    #             start_time = time.perf_counter_ns()
    #             result_divconq = ob.start_search(42)
    #             end_time = time.perf_counter_ns()
    #             gc.enable()
    #             timediff_divconq = end_time-start_time
    #             total_time_divconq+=timediff_divconq
           
    #         print('Execution time Divide and Conquer:', total_time_divconq/(1000*repetitions), 'milliseconds')

    #         #SELF-MADE TIMEIT LOGIC
    #         total_time_linear = 0 
    #         repetitions = 100
    #         result_linear =0
    #         for i in range(repetitions):
    #             gc.disable()
    #             start_time = time.perf_counter_ns()
    #             result_linear = ob.start_search_linear(42)
    #             end_time = time.perf_counter_ns()
    #             gc.enable()
    #             timediff_linear = end_time-start_time
    #             total_time_linear+=timediff_linear

    #         print('Execution time Linear:', total_time_linear/(1000*repetitions), 'milliseconds')

    #         self.assertEqual(result_divconq, solutions[14])
    #         self.assertEqual(result_linear, solutions[14])

    
        

    # def test_timer_large(self):
    #         sys. setrecursionlimit(10000)

    #         shift = 2
    #         height=15
    #         width =25

    #         a1d = np.arange(1,height*width+1)
    #         a = np.reshape(a1d, (height,width))

    #         test = IntelDevice(height,width,[],[],shift)
    #         raw_locations = [f"l{i}" for i in range(len(a1d))]
    #         raw_codes = [str(x) for x in a.reshape(-1)]
    #         enc_locations = [test.encode_message(i) for i in raw_locations]
    #         enc_codes = [test.encode_message(i) for i in raw_codes]
    #         solutions=enc_locations

    #         ob = IntelDevice(width,height, enc_locations, enc_codes, shift)
    #         ob.fill_coordinate_to_loc()
    #         ob.fill_loc_grid()

    #         # #SELF-MADE TIMEIT LOGIC
    #         # total_time_linear = 0 
    #         # repetitions = 1
    #         # result_linear =0
    #         # for i in range(repetitions):
    #         #     gc.disable()
    #         #     start_time = time.perf_counter_ns()
    #         #     result_linear = ob.divconq_search_linear(3500)
    #         #     end_time = time.perf_counter_ns()
    #         #     gc.enable()
    #         #     timediff_linear = end_time-start_time
    #         #     total_time_linear+=timediff_linear

    #         # print('Execution time Linear:', total_time_linear/(1000000*repetitions), 'milliseconds')

    #         # #SELF-MADE TIMEIT LOGIC
    #         # total_time_divconq = 0 
    #         # repetitions = 1
    #         # result_divconq =0
    #         # for i in range(repetitions):
    #         #     gc.disable()
    #         #     start_time = time.perf_counter_ns()
    #         #     result_divconq = ob.start_search(3500)
    #         #     end_time = time.perf_counter_ns()
    #         #     gc.enable()
    #         #     timediff_divconq = end_time-start_time
    #         #     total_time_divconq+=timediff_divconq
           
    #         # print('Execution time Divide and Conquer:', total_time_divconq/(1000000*repetitions), 'milliseconds')

    #         gc.disable()
    #         start_time = time.perf_counter_ns()        
    #         result_divconq = ob.start_search(width*height)
    #         end_time = time.perf_counter_ns()
    #         gc.enable()
    #         total_time_divconq = end_time-start_time
            
    #         print('Execution time Divide and Conquer:', total_time_divconq/1000000, 'milliseconds')

    #         gc.disable()
    #         start_time2 = time.perf_counter_ns()        
    #         result_linear = ob.start_search_linear(width*height)
    #         end_time2 = time.perf_counter_ns()
    #         gc.enable()
    #         total_time_linear = end_time2-start_time2
            
    #         print('Execution time Linear:', total_time_linear/1000000, 'milliseconds')

    #         self.assertEqual(result_divconq, solutions[14])
    #         self.assertEqual(result_linear, solutions[14])

    #Check if wrong input type is caught
    def test_string(self):
            a = np.array([
                
                ["a","b"],
                ["c","d"]
            ])

            shift = 2
            height=2
            width =2

            enc_locations = [
                "1101110 110010", #l0
                "1101110 110011", #l1
                "1101110 110100", #l2
                "1101110 110101"
            ]

            enc_codes = ['1100011', '1100100', '1100101', '1100110']
            solutions = [
                "1101110 110010", #l0
                "1101110 110011", #l1
                "1101110 110100", #l2
                "1101110 110101"
            ]

            ob = IntelDevice(width,height, enc_locations, enc_codes, shift)

            # values that occur in the 2d grid
            for vid, v in enumerate(a.reshape(-1)):
                result = ob.start_search(v)
                self.assertIsNone(result, solutions[vid])


    #Check if empty array error is caught
    def test_empty(self):
                #empty grid to check algortihms scope
                a = np.array([
                    
                ])

                shift = 2
                height=0
                width =0

                enc_locations = []
                enc_codes = []
                solutions = []

                ob = IntelDevice(width,height, enc_locations, enc_codes, shift)

                result = ob.start_search(1)
                self.assertIsNone(result)

    #Check if it is caught when constraints are violated
    def test_violated_constrains(self):
            #9 is not bigger than 27 and 28, hence the constraints are violated 
            a = np.array([
                [1, 10,14,22,27],
                [11,15,24,28,9],
                [12,23,32,45,55]
            ])

            shift = 2
            height=3
            width =5

            # test = IntelDevice(height,width,[],[],shift)
            # encoded_codes=[]
            #         #Iterate through all rows and columns
            # for row in range(height):
            #   for column in range(width):
            # #Add character to location dictionaryx
            #       encoded_codes.append(test.encode_message(str(a[row][column])))
            # print(encoded_codes)
            

            enc_locations = [
                 "1101110 110010", #l0
                "1101110 110011", #l1
                "1101110 110100", #l2
                "1101110 110101", #
                "1101110 110110",
                "1101110 110111",
                "1101110 111000",
                "1101110 111001",
                "1101110 111010", #l8
                "1101110 111011",
                "1101110 111100",
                "1101110 111101",
                "1101110 111110",
                "1101110 111111",
                "1101110 1000000",
                "1101110 1000001"
            ]

            enc_codes = ['110011', '110011 110010', '110011 110110', '110100 110100', '110100 111001', '110011 110011', '110011 110111', '110100 110110', '110100 111010', '111011', '110011 110100', '110100 110101', '110101 110100', '110110 110111', '110111 110111']

            solutions = [
                 "1101110 110010", #l0
                "1101110 110011", #l1
                "1101110 110100", #l2
                "1101110 110101", #
                "1101110 110110",
                "1101110 110111",
                "1101110 111000",
                "1101110 111001",
                "1101110 111010", #l8
                "1101110 111011",
                "1101110 111100",
                "1101110 111101",
                "1101110 111110",
                "1101110 111111",
                "1101110 1000000",
                "1101110 1000001"
            ]

            ob = IntelDevice(width,height, enc_locations, enc_codes, shift)
            

            # values that occur in the 2d grid
            for v in enumerate(a.reshape(-1)):
                result = ob.start_search(v)
                self.assertIsNone(result)
            
            # values that do not occur should lead to None
            for v in [0,2,18,31,48,60]:
                result = ob.start_search(v)
                self.assertIsNone(result)