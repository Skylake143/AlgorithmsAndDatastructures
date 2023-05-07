import numpy as np
import typing

class IntelDevice:
    def __init__(self, width:int, height:int, enc_locations: typing.List[str], enc_codes:typing.List[str], caesar_shift: int):
        """
        The IntelDevice object, containing all information and functions required for encoding and decoding messages,
        processing raw encoded locations, efficiently searching for locations based on codes and returning encoded
        answers.  
        #changes commit check

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

        # TODO

        new_word= msg
        new_word_l= []
        for i in range(len(new_word)):
            bin_char='{0:b}'.format(ord(new_word[i])+self.caesar_shift)
            new_word_l.append(bin_char)
        new_word_n=" ".join(new_word_l)

        return new_word_n





#string.replace(old, new, count)

        #print(self.msg)
        #for word
        #return self.msg
    
    def decode_message(self, msg: str) -> str:
        """
        A function that decodes an encoded message (the reverse of the function above). For example, given the encoded message 
        '1101101 1101010 1110001 1110001 1110100' (with the caesar shift self.caeser_shift=5), this function should return the decoded 
        message, which is 'hello'. 

        :param msg: The encoded message (string) that should be decoded
        
        Returns: the decoded message
        """

        # TODO

        b_list= msg
        new_word=b_list.split()

        for binary in new_word:
            index_b= new_word.index(binary)
            character= chr(int(binary,2)-int(self.caesar_shift))
            new_word[index_b]=character

        new_word_n="".join(new_word)
        return new_word_n





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

        decoded_loc=[]
        for i in self.enc_locations:
            decoded_loc.append(self.decode_message(i))

        coord_grid=self.coordinate_to_location
        y=0
        loc_index=0
        for line in self.loc_grid:
            x=0

            for location in line:
                coord_grid[(y,x)]= decoded_loc[loc_index]
                loc_index+= 1
                x+=1
            y+=1

        return coord_grid

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

        decoded_enc=[]
        for i in self.enc_codes:
            decoded_enc.append(self.decode_message(i))

        grid=self.loc_grid
        y=0
        loc_index=0
        for row in self.loc_grid:
            x=0
            for location in row:
                grid[y][x]= decoded_enc[loc_index]
                loc_index+= 1
                x+=1
            y+=1

        return grid



    def divconq_search(self, value: int, x_from: int, x_to: int, y_from: int, y_to: int) -> typing.Tuple[int, int]:
        """
        The divide and conquer search function. The function searches for value in a subset of self.loc_grid.
        More specifically, we only search in the x-region from x_from up to (and including) x_to and the y-region
        from y_from up to (and including) y_to. At the initial function call, x_from=0, x_to=self.width-1, y_from=0, y_to=self.height-1 ,
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
        # TODO
        #1) idea list of subrectangles:
        #2) then iterate over subrectangles
        #how to algorithm for one subrectangle?
        #y_from,x_from= package? no, then next
        #if self.width >

        #print(x_to)
        #print(y_from)
        #print(y_to)
        grid= self.fill_loc_grid()

        flag= None
        if x_to >= y_to:
            fsq_s= y_to
        else:
            fsq_s=x_to

        #fsq sidelenght of biggest possibel first square

        solution_coord= None #holder for return (evaluation)

        for diag_loc in range(fsq_s+1):
            if value > grid[diag_loc][diag_loc]:#if value is bigger than first one on the diagonal, check next biggest value on diagonal
                continue
            else: #search for the actual value in: (diag_loc, diag_loc-1),  (diag_loc, diag_loc-2),..., (diag_loc, 0) and (diag_loc-1, diag_loc), ..., (0, diag_loc)

                coord_grid=self.fill_coordinate_to_loc()
                loc_search= []

                if value== grid[diag_loc][diag_loc]: #check for (diag_loc, diag_loc)
                    solution_coord=(diag_loc,diag_loc)
                    break

                else:
                    #all possible location except (diag_loc,diagloc)
                    for latvert_loc in range(diag_loc):#what if diag_loc=0
                        loc_search.append(grid[diag_loc-(1+latvert_loc)][diag_loc])
                        loc_search.append(grid[diag_loc][diag_loc-(1+latvert_loc)])
                    index=0
                    for p_v in loc_search: #loop over all possible locations
                        if p_v== value: #if value found, transform from index of locaton list to location
                            if index%2==1:
                                solution_coord= (diag_loc,diag_loc-((index+1)/2))
                            else:
                                solution_coord=(diag_loc-((index/2)+1),diag_loc)
                            break
                        index+=1

                    break

        return solution_coord


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
        result = self.divconq_search(value, x_from=0, x_to=self.loc_grid.shape[1]-1, y_from=0, y_to=self.loc_grid.shape[0]-1)

        if result is None:
            return result
        else:
            return self.encode_message(self.coordinate_to_location[result])