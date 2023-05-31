import typing
import unittest
import numpy as np

from dynprog import DroneExtinguisher


class TestDroneExtinguisher(unittest.TestCase):
    def test_multiple_wrong_input(self):
        forest_location = (3,3)#other location than (0,0)
        bags = [-3,9,-2,3,19]    #wrong inputs: can't be negative
        bag_locations = [(i+1,2*i) for i in range(len(bags))] # tuples (i+1,i*2-1)
        liter_cost_per_km = -0.1 #wrong cost
        liter_budget_per_day = 20
        usage_cost = np.array([[1,1,0],
                            [1,1,0],
                            [1,1,0],
                            [1,1,0]])


        
        de = DroneExtinguisher(
            forest_location=forest_location,
            bags=bags,
            bag_locations=bag_locations,
            liter_cost_per_km=liter_cost_per_km,
            liter_budget_per_day=liter_budget_per_day,
            usage_cost=usage_cost
        )

        #solution: None
        de.fill_travel_costs_in_liters()
        de.dynamic_programming()
        lowest_cost = de.lowest_cost()
        self.assertIsNone(lowest_cost)


    def test_day_constraint_error(self):
        forest_location = (0,0)
        bags = [3,9,2,3,19]
        bag_locations = [(3,4) for _ in range(len(bags))] # constant travel distance 5
        liter_cost_per_km = 0.1 # now there is a constant cost of 1 liter traveling time per bag
        liter_budget_per_day = 3
        usage_cost = np.array([[1,1,0],
                             [1,1,0],
                             [1,1,0],
                             [1,1,0]])


        solution = np.inf #day constraint too small


        de = DroneExtinguisher(
            forest_location=forest_location,
            bags=bags,
            bag_locations=bag_locations,
            liter_cost_per_km=liter_cost_per_km,
            liter_budget_per_day=liter_budget_per_day,
            usage_cost=usage_cost
        )


        de.fill_travel_costs_in_liters()
        de.dynamic_programming()
        lowest_cost = de.lowest_cost()
        self.assertEqual(lowest_cost, solution)

    def test_backtracing(self):
        forest_location = (0,0)
        bags = [3,9,2,3,19]
        bag_locations = [(3,4) for _ in range(len(bags))] # constant travel distance 5
        liter_cost_per_km = 0.1 # now there is a constant cost of 1 liter traveling time per bag
        liter_budget_per_day = 20
        usage_cost = np.array([[100,1,100],
                             [100,1,100],
                             [100,1,100],
                             [100,100,1],
                             [100,100,1]])

        solution = [1,1,1,2,2] #Correct path

        de = DroneExtinguisher(
            forest_location=forest_location,
            bags=bags,
            bag_locations=bag_locations,
            liter_cost_per_km=liter_cost_per_km,
            liter_budget_per_day=liter_budget_per_day,
            usage_cost=usage_cost
        )

        de.fill_travel_costs_in_liters()
        de.dynamic_programming()
        lowest_cost = de.lowest_cost()
        backtrace_order = de.backtrace_solution()

        self.assertEqual(backtrace_order[1], solution)