######################################################

#   Solved on Thursday, 02 - 01 - 2024.

######################################################


######################################################

#   Approach I: O(m + n) Space Complexity

#   Runtime: 104ms   -   70.65%
#   Memory: 18.36MB  -   57.02%

######################################################

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = []
        cols = []

        # Storing the row and col indices if 
        # matrix[row][col] == 0
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0: 
                    rows.append(row)
                    cols.append(col)
        
        # Setting those rows with 0
        for row in rows:
            for col in range(len(matrix[0])):
                matrix[row][col] = 0
        
        # Setting those cols with 0
        for col in cols:
            for row in range(len(matrix)):
                matrix[row][col] = 0

######################################################

#   Approach II: O(1) Space Complexity

#   Runtime: 92ms   -   97.99%
#   Memory: 17.36MB  -   77.02%

######################################################

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
            We are using row 0 to store which cols need to be
            set 0 and col 0 to store which rows need to be set
            0.
            But, there is an overlap at [0,0]. If we set it to
            0, we have no way of differentiating if we need to
            set row0 to 0 or col0 to 0 or both. So, we use
            [0,0] to determine if row0 needs to be set to 0 and
            col0 var to determine if col0 needs to be set to 0.
        """
        col0 = 1
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    # Setting that we need to set row to 0.
                    matrix[row][0] = 0
                    # If col is 0, we set col0 to 0 to avoid
                    # overlap of [0,0] cell
                    if col == 0: col0 = 0
                    # Else, we set that we need to col to 0.
                    else: matrix[0][col] = 0
        
        # Setting cells to 0 based on their row and col.
        for row in range(1, len(matrix)):
            for col in range(1, len(matrix[0])):
                if matrix[0][col] == 0 or matrix[row][0] == 0: matrix[row][col] = 0
        # If row 0 needs to be 0
        if matrix[0][0] == 0:
            for col in range(len(matrix[0])):
                matrix[0][col] = 0
        # If col 0 needs to be 0
        if col0 == 0:
            for row in range(len(matrix)):
                matrix[row][0] = 0