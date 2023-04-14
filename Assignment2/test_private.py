import typing
import unittest
import numpy as np

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