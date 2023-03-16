##################################################################################
# It is not allowed to add imports here. Use these two packages and nothing else.
import numpy as np
import typing
##################################################################################


class CSP:
    def __init__(self, grid:np.ndarray, numbers: typing.Set[int], groups: typing.List[typing.List[typing.Tuple[int,int]]],
                 constraints: typing.List[typing.Tuple[int,int]]):
        
        """
        The CSP solver object, containing all information and functions required for the assignment. You do not need to change
        this function.

        :param grid: 2-d numpy array corresponding to the grid that we have to fill in. Empty squares are denoted with 0s.
        :param numbers: The set of numbers that we are allowed to use in order to fill the grid (can be any set of integers)
        :param groups: A list of cell groups (cell groups are lists of location tuples).
        :param constraints: The list of constraints for every group of cells. constraints[i] hold for groups[i]. Every
                            constraint is a tuple of the form (sum_of_elements, max_count_element) where sum_of_elements 
                            indicates what the sum must be of the elements of the given group, and max_count_element indicates
                            the maximum number of times that a number/element may occur in the given group
        """

        self.width = grid.shape[1]
        self.height = grid.shape[0]
        self.numbers = numbers
        #Sorting the numbers first is a greedier approach than using a set of numbers, since the smallest number will be used first and thus it gets less likely to run into the sum constraint
        self.sorted_numbers = sorted(self.numbers)
        self.groups = groups
        self.constraints = constraints

        self.grid = grid
        self.cell_to_groups = {(row_idx, col_idx): [] for row_idx in range(self.height) for col_idx in range(self.width)}


    def fill_cell_to_groups(self):
        """
        Function that fills in the self.cell_to_groups datastructure, which maps a cell location (row_idx, col_idx)
        to a list of groups of which it is a member. For example, suppose that cell (0,0) is member of groups 0, 1,
        and 2. Then, self.cell_to_groups[(0,0)] should be equal to [0,1,2]. This function should do this for every cell. 
        If a cell is not a member of any groups, self.cell_to_groups[cell] should be an empty list []. 
        The function does not return anything. 

        Before completing this function, make sure to read the assignment description and study the data structures created
        in the __init__ function above (self.groups and self.cell_to_groups).
        """
        #Iterate through positions in key element of cell_to_groups
        for elem in self.cell_to_groups: 

            for group in self.groups:
                #Check for every group if elem is in group
                if elem in group:
                    #If elem is in group then index of group should be added to cell_to_groups
                    index = self.groups.index(group)
                    self.cell_to_groups.get(elem).append(index)
        return 


    def satisfies_sum_constraint(self, group: typing.List[typing.Tuple[int,int]], sum_constraint: int) -> bool:
        """
        Function that checks whether the given group satisfies the given sum constraint (group smaller or equal 
        than sum). Returns True if the current group satisfies the constraint and False otherwise. 

        :param group: The list of locations [loc1, loc2, loc3,...,locN] that specify the group. Here, every loc is 
                      a tuple (row_idx, col_idx) of indices, specifying the row and column of the cell. 
        :param sum_constraint: The sum_of_elements constraint specifying that the numbers in the given group must
                               sum up to this number. This is None if there is no sum constraint for the given group. 
        """
        #Evaluates the grid values at each position (y,x) in group
        calc_sum =[self.grid[y][x] for (y,x) in group]
        #returns True if sum constraint is fulfilled and false if not
        if sum(calc_sum)<=sum_constraint:
            return True
        else: return False


    
    def satisfies_count_constraint(self, group: typing.List[typing.Tuple[int,int]], count_constraint: int) -> bool:
        """
        Function that checks whether the given group satisfies the given count constraint.
        Returns True if the current group satisfies the constraint and False otherwise. 
        Recall that the value of 0 indicates an empty cell (0s should not count towards the count constraint).

        :param group: The list of locations [loc1, loc2, loc3,...,locN] that specify the group. Here, every loc is 
                      a tuple (row_idx, col_idx) of indices, specifying the row and column of the cell. 
        :param count_constraint: Integer specifying that a given number cannot occur more than this amount of times. 
                                 This is None if there is no count constraint for the given group. 
        """
        #Return true if there are no constraints
        if count_constraint == None:return True

        #Get list of entries for every location in group 
        entries = [self.grid[y][x] for (y,x) in group]
        #Get for each number in numbers how often it occurs in
        multiplicities = [entries.count(number) for number in self.numbers]
        #Check for each multiplicity in multiplicities if it satisfies count constraint
        return all(multiplicity<=count_constraint for multiplicity in multiplicities)
    

    def satisfies_group_constraints(self, group_indices: typing.List[int]) -> bool:
        """
        Function that checks whether the constraints for the given group indices are satisfied.
        Returns True if all relevant constraints are satisfied, False otherwise. Make sure to use functions defined above. 

        :param group_indices: The indices of the groups for which we check all of the constraints 
        """
        #Iterate through indices
        for index in group_indices:
            #Check both constraints for each index and store bool in variable
            sum_constraint = self.satisfies_sum_constraint(self.groups[index],self.constraints[index][0])
            count_constraint = self.satisfies_count_constraint(self.groups[index],self.constraints[index][1])
            #Check if any output is False and return False in that case
            if sum_constraint is False or count_constraint is False:
                return False
            
        #Otherwise return True since there is no case where it outputs False
        return True

    def check_errors(self): 

        #Error double element in group
        for group in self.groups:
            dup = [x for x in group if group.count(x) > 1]
            if len(dup) is not 0:
                return True
        
        #Error group index out of grid bounds
        for group in self.groups:
            x_dim = np.size(self.grid,0)
            y_dim = np.size(self.grid, 1)
            out_of_bounds = [(x,y) for (x,y) in group if x>=x_dim or y>=y_dim]
            if len(out_of_bounds) is not 0:
                return True
        
        return False
            
    

    def search(self, empty_locations: typing.List[typing.Tuple[int, int]]) -> np.ndarray:
        """
        Recursive exhaustive search function. It tries to fill in the empty_locations with permissible values
        in an attempt to find a valid solution that does not violate any of the constraints. Instead of checking all
        possible constraints after filling in a number, it checks only the relevant group constraints using the 
        self.cell_to_groups data structure. 

        Returns None if there is no solution. Returns the filled in solution (self.grid) otherwise if a solution is found.

        :param empty_locations: list of empty locations that still need a value from self.numbers 
        """
        #Base Case: Checks if grid is already sufficiently filled
        if len(empty_locations)==0: 
            #Check constraints of all groups
            if(self.satisfies_group_constraints(range(len(self.groups)))):
                return self.grid
            else: return None

        #Recursive case
        #Get first empty location
        location = empty_locations[0]
        #Get which groups contain location
        #You should just need that in a backtracking solution, since we do not check solution right in the forloop for the exhaustive search
        #affected_indices = self.cell_to_groups.get(location)

        #For each number
        for tryout in self.numbers: 
            #Assign number to grid
            self.grid[location[0]][location[1]] = tryout
            #Recursively fill next location
            result = self.search(empty_locations[1:])
            #return result as long as constraints are fulfilled
            #Since we do not check for the constraints here (as we will do later in the backtracking solution) 
            #The code will basically fill all grid positions until the base case checks if the constraints are fulfilled; Only there it decides if it is returned None or self.grid
            if result is not None: return result
            #In case of result being None (so constraint check in base case was not succesful) we reset the location in the grid to 0 and continue with the next number
            self.grid[location[0]][location[1]] = 0

        #This return statement is just reached in case that there is no solution for the grid; according to the function describtion None should be returned then 
        return None
    
    def search_backtracking(self, empty_locations: typing.List[typing.Tuple[int, int]]) -> np.ndarray:
        """
        Recursive exhaustive search function. It tries to fill in the empty_locations with permissible values
        in an attempt to find a valid solution that does not violate any of the constraints. Instead of checking all
        possible constraints after filling in a number, it checks only the relevant group constraints using the 
        self.cell_to_groups data structure. 

        Returns None if there is no solution. Returns the filled in solution (self.grid) otherwise if a solution is found.

        :param empty_locations: list of empty locations that still need a value from self.numbers 
        """
        #Base Case: Checks if grid is already sufficiently filled
        if len(empty_locations)==0: 
            #Constraints do not need to be checked again here, since we already check them in the Recursive case loop
            return self.grid

        #Recursive case:
        #Get first empty location
        location = empty_locations[0]
        #Get which groups contain location to check them for constraints later on
        affected_indices = self.cell_to_groups.get(location)

        #For each number
        for tryout in self.numbers: 
            #Assign number to grid
            self.grid[location[0]][location[1]] = tryout
            #Check if constraints are still satisfied with new tryout, if not all further recursive calls will not be called (or in other words all subtrees will never be visited)
            if(self.satisfies_group_constraints(affected_indices)):
                #Recursively fill next location
                result = self.search_backtracking(empty_locations[1:])
                #If there is no result (so return None at the end is reached) for given tryout we continue with next tryout
                if result is not None: return result
            #In case of result being None we reset the location in the grid to 0 and continue with the next number
            self.grid[location[0]][location[1]] = 0
        
        #This return statement is just reached in case that there is no solution for the grid; according to the function describtion None should be returned then 
        return None

    def helper_get_group_complement(self, group: typing.List[typing.Tuple[int,int]], sum_constraint: int) -> bool:
        """
        Function that checks whether the given group satisfies the given sum constraint (group smaller or equal 
        than sum). Returns True if the current group satisfies the constraint and False otherwise. 

        :param group: The list of locations [loc1, loc2, loc3,...,locN] that specify the group. Here, every loc is 
                      a tuple (row_idx, col_idx) of indices, specifying the row and column of the cell. 
        :param sum_constraint: The sum_of_elements constraint specifying that the numbers in the given group must
                               sum up to this number. This is None if there is no sum constraint for the given group. 
        """

        #Evaluates the grid values at each position (y,x) in group
        calc_sum =[self.grid[y][x] for (y,x) in group]
        #Calculate complement
        complement = sum_constraint-sum(calc_sum)
        return complement

    def search_greedy_backtracking(self, empty_locations: typing.List[typing.Tuple[int, int]]) -> np.ndarray:
        """
        Recursive exhaustive search function. It tries to fill in the empty_locations with permissible values
        in an attempt to find a valid solution that does not violate any of the constraints. Instead of checking all
        possible constraints after filling in a number, it checks only the relevant group constraints using the 
        self.cell_to_groups data structure. 

        Returns None if there is no solution. Returns the filled in solution (self.grid) otherwise if a solution is found.

        :param empty_locations: list of empty locations that still need a value from self.numbers 
        """
        #Base Case: Checks if grid is already sufficiently filled
        if len(empty_locations)==0: 
            #Constraints do not need to be checked again here, since we already check them in the Recursive case loop
            return self.grid

        #Recursive case:
        #Get first empty location
        location = empty_locations[0]
        #Get which groups contain location to check them for constraints later on
        affected_indices = self.cell_to_groups.get(location)
        #Find out the maximum allowed number by calculating the complement of max_sum_constraint and the sum of already filled elements; in case that max_allowed_number<min(numbers) we effectively skip the whole code and save a lot of time; otherways we just check necessary elements
        max_allowed_number = np.inf
        if len(affected_indices) is not 0:
            max_allowed_number = min([self.helper_get_group_complement(self.groups[index], self.constraints[index][0]) for index in affected_indices])
            #Instead of using numbers as in exhaustive search and backtracking, we use a sorted list of the set numbers; this is greedier since the algorithms begins checking the lowest number and thus runs less likely in the sum constraint
            sorted_numbers_smaller_than_max = [x for x in self.sorted_numbers if x <= max_allowed_number]
        else: 
            sorted_numbers_smaller_than_max = self.sorted_numbers

        #For each number
        for tryout in sorted_numbers_smaller_than_max: 
            #Assign number to grid
            self.grid[location[0]][location[1]] = tryout
            #Check if constraints are still satisfied with new tryout, if not all further recursive calls will not be called (or in other words all subtrees will never be visited)
            if(self.satisfies_group_constraints(affected_indices)):
                #Recursively fill next location
                result = self.search_greedy_backtracking(empty_locations[1:])
                #If there is no result (so return None at the end is reached) for given tryout we continue with next tryout
                if result is not None: return result
            
        #In case of result being None we reset the location in the grid to 0 and continue with the next number
        #Since end of for loop is anyway just reached when None is returned we can also reset the location to 0 here to make the algorithm more greedy
        self.grid[location[0]][location[1]] = 0
        #This return statement is just reached in case that there is no solution for the grid; according to the function describtion None should be returned then 
        return None
    

    def start_search(self):
        """
        Non-recursive function that starts the recursive search function above. It first fills the cell_to_group
        data structure and computes the empty locations. Then, it starts the recursive exhaustive search procedure. 
        The result is None if there is no solution possible. Otherwise, it returns the grid that is a solution.

        You do not need to change this function.
        """

        self.fill_cell_to_groups()
        empty_locations = [(row_idx, col_idx) for row_idx in range(self.height) for col_idx in range(self.width) if self.grid[row_idx,col_idx]==0]
        if self.check_errors() is True:
            return None
        return self.search(empty_locations)
    
    def start_search_backtracking(self):
        """        
        Non-recursive function that starts the recursive search function above. It first fills the cell_to_group
        data structure and computes the empty locations. Then, it starts the recursive backtracking search procedure. 
        The result is None if there is no solution possible. Otherwise, it returns the grid that is a solution.

        You do not need to change this function.
        """

        self.fill_cell_to_groups()
        empty_locations = [(row_idx, col_idx) for row_idx in range(self.height) for col_idx in range(self.width) if self.grid[row_idx,col_idx]==0]
        if self.check_errors() is True:
            return None
        return self.search_backtracking(empty_locations)
    
    def start_search_greedy_backtracking(self):
        """        
        Non-recursive function that starts the recursive search function above. It first fills the cell_to_group
        data structure and computes the empty locations. Then, it starts the recursive backtracking search procedure. 
        The result is None if there is no solution possible. Otherwise, it returns the grid that is a solution.

        You do not need to change this function.
        """

        self.fill_cell_to_groups()
        empty_locations = [(row_idx, col_idx) for row_idx in range(self.height) for col_idx in range(self.width) if self.grid[row_idx,col_idx]==0]
        if self.check_errors() is True:
            return None
        return self.search_greedy_backtracking(empty_locations)
