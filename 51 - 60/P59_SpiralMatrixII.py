######################################################

#   Solved on Wednesday, 13 - 04 - 2022.

######################################################


######################################################

#   Runtime: 32ms   -   91.74%
#   Memory: 13.9MB  -   85.84%

######################################################

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        matrix = [[0] * n for _ in range(n)]
        # Values of direction will be:
        # 1 = right
        # 2 = left
        # 3 = up
        # 4 = down
        # This var tell us the current direction we are going
        direction = 1
        # Boundaries of the spiral matrix. Initialising left to left end i.e 0,
        # right to right end i.e; n - 1, top to top end i.e; 0 and botton to botton
        # end i.e; n - 1
        left = 0
        right = n - 1
        top = 0
        bottom = n - 1
        # row, col at which we have to insert the value
        row = 0
        col = 0
        # Looping n^2 times
        for num in range(1, n * n + 1):
            # Inserting num value at row, col
            matrix[row][col] = num
            # If we are going in "right" direction
            if direction == 1: 
                # To get next cell, we have to increase col value.
                col += 1
                # If col reached right boundary, in next iteration we can't go right
                # According to spiral logic, we have to go in downward direction
                if col == right:
                    # Since top boundary row is completely inserted, increasing it
                    top += 1
                    # Changing direction to down
                    direction = 4
            # If we are going in "left" direction
            elif direction == 2: 
                # To get next cell, we have to decrease col value.
                col -= 1
                # If col reached left boundary, in next iteration we can't go left
                # According to spiral logic, we have to go in upward direction
                if col == left:
                    # Since bottom boundary row is completely inserted, decreasing it
                    bottom -= 1
                    # Changing direction to up
                    direction = 3
            # If we are going in "up" direction
            elif direction == 3: 
                # To get next cell, we have to decrease row value.
                row -= 1
                # If row reached top boundary, in next iteration we can't go up
                # According to spiral logic, we have to go in right direction
                if row == top:
                    # Since left boundary col is completely inserted, increasing it
                    left += 1
                    # Changing direction to right
                    direction = 1
            # If we are going in "down" direction
            else: 
                # To get next cell, we have to increase row value.
                row += 1
                # If row reached botton boundary, in next iteration we can't go down
                # According to spiral logic, we have to go in left direction
                if row == bottom:
                    # Since right boundary col is completely inserted, decreasing it
                    right -= 1
                    # Changing direction to left
                    direction = 2
    
        return matrix