######################################################

#   Solved on Tuesday, 24 - 08 - 2021.

######################################################


######################################################

#   Runtime: 88ms   -   95.41%
#   Memory: 14.1MB  -   97.27%

######################################################

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
            The logic is, we take 3 list of sets horizontal, vertical, grid of len 9
            which stores the chars present in the board at each row i, col j, grid
            (i // 3) * 3 + (j // 3). We loop through the board and at every index i,j
            If current char at index i, j is already present in either horizontal[i] 
            or vertical[j] or grid[(i // 3) * 3 + (j // 3)] then that means there is 
            a duplicate entry. So return False. If we get out of loop that means there
            is no duplicate entry. So we return True
        """
        horizontal = [None] * 9
        vertical = [None] * 9
        grid = [None] * 9
        
        for i in range(9):
            for j in range(9):
                
                if board[i][j] == ".": continue
                    
                if horizontal[i] == None: horizontal[i] = set()
                elif board[i][j] in horizontal[i]: return False
                
                if vertical[j] == None: vertical[j] = set()
                elif board[i][j] in vertical[j]: return False
                
                gridIndex = (i // 3) * 3 + (j // 3)
                if grid[gridIndex] == None: grid[gridIndex] = set()
                elif board[i][j] in grid[gridIndex]: return False
                
                horizontal[i].add(board[i][j])
                vertical[j].add(board[i][j])
                grid[gridIndex].add(board[i][j])
            
        return True