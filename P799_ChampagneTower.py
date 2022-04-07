######################################################

#   Solved on Friday, 04 - 03 - 2022.

######################################################


######################################################

#   Runtime: 88ms   -   97.57%
#   Memory: 13.9MB  -   95.15%

######################################################

class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        # Creating a glasses stack to store the quantities of liquid in each glass of
        # the pyramid. Initialsing with only 1 row with a single column having all the
        # liquid
        glassesStack = [[poured]]
        # isLeft helps us in finding whether next row of current row has liquid > 1
        # in any of the next row glasses. If not it is a waste of time to loop through
        # till we reach the required row right since we will be getting all 0's from
        # next row to query row because there is not overflow in next row
        # We initialise with True if given poured is not 0. If it is 0, we can't even
        # fill first glass
        isLeft = poured != 0
        # To track the row we are at
        index = 0
        # While next row has some glasses which are overflowing and we haven't reached
        # the requied query row
        while isLeft and index < query_row:
            # Considering next row has not overflow to begin with
            isLeft = False
            # Adding next row to stack with length 1 greater than current row length
            glassesStack.append([0] * (index + 2))
            # Looping through current row
            for j in range(index + 1):
                # If there is a overflow at glass j
                if glassesStack[index][j] > 1:
                    # Half of overflow will go to its left glass which has same index
                    # as this glass i.e; j
                    glassesStack[-1][j] += (glassesStack[index][j] - 1) / 2
                    # Another half goes to right glass which has index j + 1
                    glassesStack[-1][j + 1] += (glassesStack[index][j] - 1) / 2
                    # Finding whether any of the left or right glasses overflowed
                    # and updating isLeft accordingly
                    isLeft = isLeft or glassesStack[-1][j] > 1 or glassesStack[-1][j + 1] > 1
                    # After overflow glass at index j takes only quantity 1 right
                    glassesStack[index][j] = 1
            # Going to next row
            index += 1
        # If isLeft became false before we reached query_row, no liquid is filled in 
        # that query_glass. So, return 0
        if index < query_row: return 0
        # If quantity at query_row and query_glass > 1, that means there is still overflow
        # So, it will have quantity 1 and remaining flows to next rows which are not our 
        # concern
        # Else, we return the quantity present in that location
        return glassesStack[query_row][query_glass] if glassesStack[query_row][query_glass] < 1 else 1
