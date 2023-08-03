######################################################

#   Solved on Sunday, 24 - 10 - 2021.

######################################################


######################################################

#   Runtime: 1412ms   -   94.74%
#   Memory: 14.2MB  -   71.98%

######################################################

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        # Below code will help in reducing time complexity significantly.
        # What below code does is, it creates a set with all chars present in board
        # and then it will check whether all chars in word are present in board
        # If a char in word is not present in the board, we can't find the word in 
        # board. So we return False
        # Without these lines of code, I got a Time Complexity of 8000+ ms
        # After adding these lines of code, my TC reduced to just 1400+ ms
        # Why this drastic change is, since we are checking all possible strings
        # using a backtracking paradigm, there will be some cases where we go to so
        # much deep just to find the required char is not even present in the board
        # So we are eliminating it before hand.
        characters = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] not in characters: characters.add(board[i][j])
        
        for s in word: 
            if s not in characters: return False
        
        def dfs(row, col, index, visited):
            # index represents current index of word string
            # Checking for out of bounds indices and returning False
            if row < 0 or row > len(board) - 1 or col < 0 or col > len(board[0]) - 1: return False
            # If we already visited current cell, return False
            if (row, col) in visited: return False
            # If char at cell (row, col) matches with word[index] we go next char
            # in all the 4 directions
            if board[row][col] == word[index]:
                visited.add((row, col))
                # If we reach end of word return Trur
                if index == len(word) - 1: return True
                isExist = (
                            dfs(row, col - 1, index + 1, visited) or 
                            dfs(row, col + 1, index + 1, visited) or
                            dfs(row - 1, col, index + 1, visited) or 
                            dfs(row + 1, col, index + 1, visited)
                       )   
                # Why we are removing at the end is, we might encounter this cell
                # again in some other path if this path didn't give us required 
                # word. In that path, we haven't yet visited the cell right. So, we
                # are removing it.
                visited.remove((row, col))
                return isExist
            
            return False
        
        # Running DFS when the char in the cell (i,j) matches with word[0] i.e; 
        # starting of the word
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    visited = set()
                    if dfs(i, j, 0, visited): return True
        
        return False