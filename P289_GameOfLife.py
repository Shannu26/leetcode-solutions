######################################################

#   Solved on Friday, 22 - 10 - 2021.

######################################################


######################################################

#   Time Efficient solution

#   Runtime: 28ms   -   95.74%
#   Memory: 14.8MB  -   11.78%

######################################################

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        """
            Logic is, we do a dfs traversal starting from 0,0. In each traversal
            we find count of live neighbours for position i,j. Then, instead of 
            mutating the board[i][j] we go to next traversal in 8 directions. When
            all those traversals are completed, we can be sure that all its neighbours
            have accessed its current value. So, now we mutate board[i][j], using 
            count of live neighbours we had already found before these 8 traversals.
        """
        # Set to keep track of already visited (i,j) pairs
        visited = set()
        
        def dfs(i, j):
            # Already visited case
            if (i,j) in visited: return 
            # i out of bounds case
            if i < 0 or i > len(board) - 1: return 
            # j out of bounds case
            if j < 0 or j > len(board[0]) - 1: return
                
            count = 0
            # All 8 neighbours
            if i > 0 and board[i - 1][j]: count += 1
            if j > 0 and board[i][j - 1]: count += 1
            if i < len(board) - 1 and board[i + 1][j]: count += 1
            if j < len(board[0]) - 1 and board[i][j + 1]: count += 1
            if i > 0 and j > 0 and board[i - 1][j - 1]: count += 1
            if i > 0 and j < len(board[0]) - 1 and board[i - 1][j + 1]: count += 1
            if i < len(board) - 1 and j > 0 and board[i + 1][j - 1]: count += 1
            if i < len(board) - 1 and j < len(board[0]) - 1 and board[i + 1][j + 1]: count += 1
            # Adding (i,j) to visited pair
            visited.add((i,j))
            # 8 neighbouring traversals
            dfs(i - 1,j)
            dfs(i,j - 1)
            dfs(i + 1,j)
            dfs(i,j + 1)
            dfs(i - 1,j - 1)
            dfs(i - 1,j + 1)
            dfs(i + 1,j - 1)
            dfs(i + 1,j + 1)
            # Updating board[i][j] using the rules given
            if board[i][j]:
                if count < 2 or count > 3: board[i][j] = 0
            else:
                if count == 3: board[i][j] = 1
        
        dfs(0,0)

######################################################

#   Optimal solution

#   Runtime: 29ms   -   86.35%
#   Memory: 14.1MB  -   89.97%

######################################################

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        """
            Logic is instead of mutating the cells to 0 or 1 if the rules given are
            met, we place 2 or -1 where 2 is placed if board[i][j] is 1 and rules are
            met, and -1 is placed if board[i][j] is 0 and rule is met

            Now, for its neighbours if it has a value of 2, we can infer that, it
            previous had a value of 1, since we placed 2 if board[i][j] is 1 and rules 
            are met. So board[k][l] > 0 condition is used instead of board[k][l] == 1

            Finally we replace 2 with 0 and -1 with 1
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                count = 0
                
                if i > 0 and board[i - 1][j] > 0: count += 1
                if j > 0 and board[i][j - 1] > 0: count += 1
                if i < len(board) - 1 and board[i + 1][j] > 0: count += 1
                if j < len(board[0]) - 1 and board[i][j + 1] > 0: count += 1
                if i > 0 and j > 0 and board[i - 1][j - 1] > 0: count += 1
                if i > 0 and j < len(board[0]) - 1 and board[i - 1][j + 1] > 0: count += 1
                if i < len(board) - 1 and j > 0 and board[i + 1][j - 1] > 0: count += 1
                if i < len(board) - 1 and j < len(board[0]) - 1 and board[i + 1][j + 1] > 0: count += 1

                if board[i][j]:
                    if count < 2 or count > 3: board[i][j] = 2
                else:
                    if count == 3: board[i][j] = -1
        # Replacing 2 with 0 and -1 with 1
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 2: board[i][j] = 0
                if board[i][j] == -1: board[i][j] = 1