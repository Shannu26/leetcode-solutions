######################################################

#   Solved on Monday, 11 - 04 - 2022.

######################################################


######################################################

#   Runtime: 179ms   -   81.06%
#   Memory: 14.3MB  -   61.56%

######################################################

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        # If k > size of grid, we waste n = len(grid) * len(grid[0]) iterations out of
        # k iterations, just to again reach the original grid state. To avoid it, getting
        # the reaminder of k % size
        k = k % (len(grid) * len(grid[0]))
        # Declaring the result array
        shiftedGrid = [[0] * len(grid[0]) for _ in range(len(grid))]
        # Logic is, we place each row, col element, k places away right.
        # Let's say if we move row, col element k places to right, it has 2 cases
        # a) It falls in same row
        # b) It goes to another row
        # If we move an element at row, col so that it exceeds the column size
        # it will go to another row
        # To know whether it goes to next row or not, we can divide the new col
        # position by column size
        #   (col + k) // len(grid[0])
        # We have to add this to our row position, since, new row val will be
        # (col + k) // len(grid[0]) positions away from current row
        # Now, we have 2 cases. 
        # a) row doesn't exceed row size
        # b) row exceed row size. In this case we have to go to the top row and come
        # one by one right. So, 
        #   row + (col + k) // len(grid[0]) - len(grid)
        # To get the column position, we can take remainder of above operation
        #   (col + k) % len(grid[0])
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                newRow = row + (col + k) // len(grid[0])
                newCol = (col + k) % len(grid[0])
                if newRow >= len(grid):
                    newRow -= len(grid)
                
                shiftedGrid[newRow][newCol] = grid[row][col]
        
        return shiftedGrid