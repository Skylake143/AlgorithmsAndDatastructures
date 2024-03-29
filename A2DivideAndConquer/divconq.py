import numpy as np
import typing

class IntelDevice:
    def __init__(self, width:int, height:int, enc_locations: typing.List[str], enc_codes:typing.List[str], caesar_shift: int):
        """
        The IntelDevice object, containing all information and functions required for encoding and decoding messages,
        processing raw encoded locations, efficiently searching for locations based on codes and returning encoded
        answers.  

        :param width: The width (number of columns) of the 2D distance/location grid (self.loc_grid) that we have to fill in
        :param height: The height (number of rows) of the 2D distance/location grid (self.loc_grid) that we have to fill in
        :param enc_locations: A list of encoded location names that correspond to the locations in self.loc_grid
        :param enc_codes: A list of encoded codes (ints) that have to be entered into self.loc_grid
        :param caesar_shift: The caesar shift constant used to encode messages. You may assume this will always be in the set 
                             {0,1,...,26}. We do NOT use modulo calculations for our caesar cipher. 

        You do not need to change this function
        """

        self.width = width
        self.height = height
        self.enc_locations = enc_locations
        self.enc_codes = enc_codes
        self.caesar_shift = caesar_shift

        self.loc_grid = np.zeros((height, width))
        self.coordinate_to_location = dict() # maps locations (y,x) to their names 


    def encode_message(self, msg:str) -> str:
        """
        A function that encodes a given string using a simplified form of caesar cipher (without using modulo). Every character of the string will be 
        transformed into the ordinal/numerical representation and encoded by shifting the number with self.caesar_shift 
        (through addition). Afterward, the shifted numbers are transformed into bitstring representation.

        For example, suppose we want to encode the message 'hello' with a caesar shift of 5. 
        The corresponding encoded message (output of this function) would be '1101101 1101010 1110001 1110001 1110100'. Note that the 
        number of bitstrings separated by spaces is equal to the number of characters of the string 'hello'. 
        Let's look at the first character 'h'. Its ordinal representation is 104. We shift its representation by 5, giving us 109. 
        109 is then transformed into a bitstring, which gives us 1101101 (the first bitstring in the encoded message). 

        Hints: the following built-in Python functions may be of use
          - ord(x): takes a character x as input and returns the ordinal representation
          - '{0:b}'.format(x): transforms a number x into a bitstring

        :param msg: The input message (string) that should be encoded
        
        Returns: the encoded message
        """
        #Transform from string to list of numerals
        ordinal = [ord(charac) for charac in msg]
        #Perform ceasar shift
        ordinal_ceasar_shift = [i+self.caesar_shift for i in ordinal]
        #Transform list of numerals into list of bitstrings
        binary_ceasar_shift = ["{0:b}".format(i) for i in ordinal_ceasar_shift]
        #Concatenate list into string
        string_binary= " ".join(binary_ceasar_shift)
        return string_binary

    
    def decode_message(self, msg: str) -> str:
        """
        A function that decodes an encoded message (the reverse of the function above). For example, given the encoded message 
        '1101101 1101010 1110001 1110001 1110100' (with the caesar shift self.caeser_shift=5), this function should return the decoded 
        message, which is 'hello'. 

        :param msg: The encoded message (string) that should be decoded
        
        Returns: the decoded message
        """

        #Transform string into list of bitstrings
        binaries_list = msg.split(' ')
        #Transfrom bitstring into integer
        ordinal_ceasarshifted = [int(i,2) for i in binaries_list]
        #Perform inverse ceasar_shift
        ordinals = [i-self.caesar_shift for i in ordinal_ceasarshifted]
        #
        characters = [chr(charac) for charac in ordinals]
        character_string = ''.join(characters)
        return character_string


    def fill_coordinate_to_loc(self):
        """
        Function that fills the data structure self.coordinate_to_location. It maps every (y,x) tuple in self.loc_grid
        to the corresponding decoded location (determined from self.enc_locations). The list of encoded locations wrap
        around the rows of self.loc_grid from left to right and top to bottom. For example, if we have a 2x2 loc_grid and 
        self.enc_locations = [self.encode_message('a'), self.encode_message('b'), self.encode_message('c'), self.encode_message('d')], 
        then the mapping should be:
          (0,0) -> 'a'
          (0,1) -> 'b'
          (1,0) -> 'c'
          (1,1) -> 'd'

        The function does not return anything. It simply fills the self.coordinate_to_location data structure with the right mapping.
        """

        #Iterate through all rows and columns
        for row in range(self.height):
          for column in range(self.width):
        #Add character to location dictionary
              self.coordinate_to_location.update({(row, column):self.decode_message(self.enc_locations[row*self.width+column])})
        return 

    def fill_loc_grid(self):
        """
        Function that fills the data structure self.loc_grid with the codes found in self.enc_codes. Note that
        these codes have to be decoded using self.decode_message(). The encoded codes wrap around self.loc_grid 
        from left to right, and from top to bottom. For example, if we have 
        self.enc_codes = [self.encode_message('10'), self.encode_message('15'), self.encode_message('11'), self.encode_message('16')],
        the following loc_grid should be created/filled in:
          [[10,15],
           [11,16]]

        The function does not return anything. It simply fills the self.loc_grid data structure with the decoded codes.
        """

        #Iterate through all rows and columns
        for row in range(self.height):
          for column in range(self.width):
        #Add character to location dictionaryx
              self.loc_grid[row, column] = self.decode_message(self.enc_codes[row*self.width+column])
        return 

    #Method checks if constraints are fulfilled that elements in rows and columns are sorted 
    def check_constraints(self):
        for columns in range(self.width):
            row = self.loc_grid[:, columns]
            if (row != np.sort(row)).all() : return False 

        for rows in range(self.height):
            column = self.loc_grid[rows,: ]
            if (column != np.sort(column)).all(): return False
        return True

    def divconq_search(self, value: int, x_from: int, x_to: int, y_from: int, y_to: int):
        """
        The divide and conquer search function. The function searches for value in a subset of self.loc_grid.
        More specifically, we only search in the x-region from x_from up to (and including) x_from and the y-region
        from y_from up to (and including) y_to. At the initial function call, x_from=0, x_to=self.width-1, y_from=0, y_to=self.height-1,
        meaning that we search over the entire 2d grid self.loc. 
        This function recursively calls itself on smaller subproblems (subsets/subrectangles of the 2d grid) and combines the solutions
        to these subproblems in order to find the solution to the complete initial problem.

        Note: this function should be more efficient than a naive search that iterates over every cell until the value is found. 
        Thus, make sure design a proper divide and conquer strategy for this. A too simplistic strategy (search over every cell in the grid) 
        will not lead to a passing grade. Please consult the TAs before handing in the assignment whether your approach is good. 

        :param value: The value that we are searching for in the subrectangle specified by (x_from, x_to, y_from, y_to)
        :param x_from: The leftmost x coordinate of the subrectangle that we are searching over
        :param x_to: The rightmost x coordinate of the subrectangle we are searching over
        :param y_from: The topmost y coordinate of the subrectangle we are searching over
        :param y_to: The bottom y coordinate of the subrectangle we are searching over

        Note that the following two constraints hold:
          1. x_from <= x_to
          2. y_from <= y_to

        Returns:
          None if the value does not occur in the subrectangle we are searching over
          A tuple (y,x) specifying the location where the value was found (if the value occurs in the subrectangle)
          """
        #Fille loc_grid with package codes 
        self.fill_loc_grid()    
        #Check if constraints are fulfilled
        if (self.check_constraints() is False): return None

        
        #If rectangle Boundaries are hit 
        if y_from > y_to and x_from > x_to:
          return None

        #Hitting bottom boundary and continue searching right leftover
        if y_from > y_to:
            #Search remaining subrectangle
            location = self.divconq_search(value, x_from+1, x_to, 0, y_to)
            return location

        #Hitting right boundary and continue searching leftover beneath
        if x_from > x_to:
            location = self.divconq_search(value, 0, x_to, y_from+1, y_to)
            return location
        
        #Found value on diagonal that is traversed
        if self.loc_grid[y_from][x_from] == value: return (y_from, x_from)

        #If entry on diagonal is bigger than value, check all elements that are left and above (according to provided constraints)
        if self.loc_grid[y_from][x_from] >= value and y_from >0 and x_from >0:
            for i in range(0,x_from):
                if self.loc_grid[y_from][i] == value:
                  return (y_from, i)
            for j in range(0,y_from):
                if self.loc_grid[j][x_from] == value:
                    return (j, x_from)
        
        #If not found continue with other leftover rectangles
        location = self.divconq_search(value, x_from+1, x_to, y_from+1, y_to)
        return location

    def divconq_search_linear(self, value: int):
        """
        The linear search function. The function iterates through all elements in self.loc_grid and checks whether the value occurs in self.loc_grid. The function should be slower than the 
        """
        decoded_messages = [self.decode_message(code) for code in self.enc_codes]
        numerics = [message.isnumeric() for message in decoded_messages]
        if False in numerics: return None

        #Fille loc_grid with package codes 
        self.fill_loc_grid()    
        #Check if constraints are fulfilled
        if (self.check_constraints() is False): return None

        #Iterate through all rows and columns
        for column in range(self.width):
          for row in range(self.height):
              if self.loc_grid[row][column]==value: return (row,column)

        return None
        
    

    def start_search(self, value) -> str:
        """
        Non-recursive function that starts the recursive divide and conquer search function above. You can assume
        that self.coordinate_to_location and self.loc_grid have already been filled before this function is called (so 
        make sure not to call them again in this function). 
        
        :param value: The value that we are searching for in self.loc_grid

        Returns:
          None if the value does not occur in self.loc_grid
          The encoded location of where the value was found. Note that the location is not the (y,x) tuple but the
          corresponding name of the location (encoded with self.encode_message). 
        """

        # process raw locations with caesar shift, 
        # construct the loc_grid and start the search
        
        #Check if elements in encoded message are only numerics
        decoded_messages = [self.decode_message(code) for code in self.enc_codes]
        numerics = [message.isnumeric() for message in decoded_messages]
        if False in numerics: return None
        result = self.divconq_search(value, x_from=0, x_to=self.loc_grid.shape[1]-1, y_from=0, y_to=self.loc_grid.shape[0]-1)

        if result is None:
            return result
        else:
            return self.encode_message(self.coordinate_to_location[result])
        
    def start_search_linear(self, value) -> str:
        """
        Non-recursive function that starts the recursive divide and conquer search function above. You can assume
        that self.coordinate_to_location and self.loc_grid have already been filled before this function is called (so 
        make sure not to call them again in this function). 
        
        :param value: The value that we are searching for in self.loc_grid

        Returns:
          None if the value does not occur in self.loc_grid
          The encoded location of where the value was found. Note that the location is not the (y,x) tuple but the
          corresponding name of the location (encoded with self.encode_message). 
        """

        # process raw locations with caesar shift, 
        # construct the loc_grid and start the search
        
        #Check if elements in encoded message are only numerics
        # decoded_messages = [self.decode_message(code) for code in self.enc_codes]
        # numerics = [message.isnumeric() for message in decoded_messages]
        # if False in numerics: return None
        result = self.divconq_search_linear(value)

        if result is None:
            return result
        else:
            return self.encode_message(self.coordinate_to_location[result])
