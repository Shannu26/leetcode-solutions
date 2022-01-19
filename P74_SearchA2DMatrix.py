######################################################

#   Solved on Wednesday, 27 - 10 - 2021.

######################################################


######################################################

#   Runtime: 36ms   -   97.29%
#   Memory: 14.5MB  -   96.19%

######################################################

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
            Logic is, since matrix is sorted, we can be sure that if matrix[row][0] >
            target, we can't find target in any row from row to end of matrix.
            So, we first do a binary search only on first column to find the row
            in which target value will present if that target is actually present in the
            matrix.

            Then, we perform a binary search on that row to check if target is present
            else, we return False
        """
        rowLow = 0
        rowHigh = len(matrix) - 1
        # Binary Search on column 0
        while rowLow <= rowHigh:
            rowMid = (rowLow + rowHigh) // 2
            if matrix[rowMid][0] == target: return True
            elif matrix[rowMid][0] > target: rowHigh = rowMid - 1
            else: rowLow = rowMid + 1
        
        row = rowHigh
        
        colLow = 0
        colHigh = len(matrix[0]) - 1
        # Binary search on found row
        while colLow <= colHigh:
            colMid = (colLow + colHigh) // 2
            if matrix[row][colMid] == target: return True
            elif matrix[row][colMid] > target: colHigh = colMid - 1
            else: colLow = colMid + 1
        
        return False