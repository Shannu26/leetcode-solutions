######################################################

#   Solved on Friday, 26 - 11 - 2021.

######################################################


######################################################

#   Runtime: 52ms   -   92.02%
#   Memory: 14.1MB  -   99.61%

######################################################

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if numRows == 1: return s
        
        strings = [""] * numRows
        # direction determines whether to add 1 to index or subtract 1 from index
        direction = 1
        # index will be the index of strings array to which we should add the next char
        index = 0
        
        for char in s:
            # Adding current char to particular index of strings array
            strings[index] += char
            # Moving index to next position
            index += direction
            # If index became -1, we went out of the left bounds of strings array
            # That means previously we added char to 0th index, so in next iteration
            # we should add to index 1. And we should go downwards. So we make
            # index = 1 and direction = 1
            if index == -1:
                index = 1
                direction = 1
            # If index became numRows, we went out of the right bounds of strings array
            # That means previously we added char to last index of strings array, so 
            # in next iteration we should add to last but one index which is 
            # numRows - 2. And we should go upwards. So we make
            # index = numRows - 1 and direction = -1   
            elif index == numRows:
                index = numRows - 2
                direction = -1
        
        # Concatenating all strings in strings array, separated by empty string
        return "".join(strings)