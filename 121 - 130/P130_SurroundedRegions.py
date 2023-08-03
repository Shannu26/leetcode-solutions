######################################################

#   Solved on Thursday, 13 - 01 - 2022.

######################################################


######################################################

#   Runtime: 120ms   -   99.84%
#   Memory: 15.4MB  -   97.12%

######################################################

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        """
            If we observe, we can infer that any cells having a path to any of the
            edge cells via 'O' won't have 4 sides of 'X'.
            So, what we can do is find paths starting from edge cells having 'O' and
            set 'X' to remainging 'O' cells since they are not part of these paths.
            To keep track of cells having connection to edge cells, we set 'Y' in place
            of 'O' for those cells.
            We can use bfs to do the traversal
        """
        def bfs(x, y):
            # To store next cells
            queue = [(x,y)]
            # To avoid traversing duplicate cells
            visited = set()
            visited.add((x,y))
            while queue:
                (x, y) = queue.pop(0)
                # Setting "Y" in place of "O"
                board[x][y] = 'Y'
                # Top cell of current cell
                if x > 0 and (x - 1, y) not in visited and board[x - 1][y] == 'O':
                    visited.add((x - 1, y))
                    queue.append((x - 1, y))
                # Bottom cell of current cell
                if x < len(board) - 1 and (x + 1, y) not in visited and board[x + 1][y] == 'O':
                    visited.add((x + 1, y))
                    queue.append((x + 1, y))
                # Left cell of current cell
                if y > 0 and (x, y - 1) not in visited and board[x][y - 1] == 'O':
                    visited.add((x, y - 1))
                    queue.append((x, y - 1))
                # Right cell of current cell
                if y < len(board[0]) - 1 and (x, y + 1) not in visited and board[x][y + 1] == 'O':
                    visited.add((x, y + 1))
                    queue.append((x, y + 1))
        
        # Top row of the grid
        for j in range(len(board[0])):
            if board[0][j] == 'O': bfs(0, j)
        # Bottom rom of the grid
        for j in range(len(board[0])):
            if board[-1][j] == 'O': bfs(len(board) - 1, j)
        # Left column of the grid
        for i in range(len(board)):
            if board[i][0] == 'O': bfs(i, 0)
        # Right column of the grid
        for i in range(len(board)):
            if board[i][-1] == 'O': bfs(i, len(board[0]) - 1)
        # Looping through the grid and changing "Y" to "O", since "Y" means that cell
        # is a part of the path from edge cells and they won't be overtaken by "X"
        # Else, "O" cells will have "X" cells in all sides. So they will change to "X"
        # So, we put "X" in remaining cells  
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'Y': board[i][j] = 'O'
                else: board[i][j] = 'X'

