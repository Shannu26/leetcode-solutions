######################################################

#   Solved on Saturday, 08 - 03 - 2024.

######################################################


######################################################

#   Approach - I: Using 2-D Array

#   Runtime: 91ms   -   77.65%
#   Memory: 20.13MB  -   31.87%

######################################################

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
            If we observe we can say that minimum number of moves
            required to get word2 from word1 depends on the subproblems.
            To provide more context, it depends on the 3 possible moves
            a) Add a character
            b) Deleting a character
            c) Replacing a character
            Let's say we are at index1 of word1 and index2 of word2,
            EQUAL CASE: 
            If word1[index1] = word2[index2], we don't have to make any moves, 
            number of moves required = number of moves required to get word2[0 to index2 - 1] 
            from word1[0 to index1 - 1]
            UNEQUAL CASE:
            a) If we are adding a character i.e; adding word2[index2] to word1,
            number of moves required = 1 (Since we are adding a character) + 
            number of moves required to get word2[0 to index2 - 1] from word1[0 to index1]
            b) If we are deleting a character i.e; deleting word1[index1],
            number of moves required = 1 (Since we are deleting a character) + 
            number of moves required to get word2[0 to index2] from word1[0 to index1 - 1]
            c) If we are replacing a character i.e; we are replacing word1[index1] with
            word2[index2], number of moves required = 1 (Since we are replacing a character) +
            number of moves required to get word2[0 to index2 - 1] from word1[0 to index1 - 1]

            
        """
        # 2-D Dp array with first row representing how to get word2[0 to index2] from empty string
        # and first col representing how to get empty string from word1[0 to index1]
        dp = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]
        # Number of moves required to convert a string to empty string = number of character to 
        # delete
        for index1 in range(len(dp)):
            dp[index1][0] = index1
        # Number of moves required to convert an empty string to string = number of character to 
        # add
        for index2 in range(len(dp[0])):
            dp[0][index2] = index2

        for index1 in range(1, len(dp)):
            for index2 in range(1, len(dp[0])):
                # EQUAL CASE: 
                # number of moves required = number of moves required to get word2[0 to index2 - 1] 
                # from word1[0 to index1 - 1] is stored in dp[index1 - 1][index2 - 1]
                if word1[index1 - 1] == word2[index2 - 1]: 
                    dp[index1][index2] = dp[index1 - 1][index2 - 1]
                # UNEQUAL CASE:
                # Case a) is stored in dp[index1][index2 - 1]
                # Case b) is stored in dp[index1 - 1][index2]
                # Case c) is stored in dp[index1 - 1][index2 - 1]
                # Since we want min moves, we take min of those 3 and add 1.
                else:
                    dp[index1][index2] = min(
                        dp[index1 - 1][index2], 
                        dp[index1][index2 - 1],
                        dp[index1 - 1][index2 - 1]) + 1
        
        return dp[-1][-1]

######################################################

#   Approach - II: Using 1-D Array

#   Runtime: 91ms   -   77.65%
#   Memory: 16.47MB  -   98.86%

######################################################

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
            The logic is same as above. But, if we observe at any point of time
            we are only using the current row or the row above. So, why waste our 
            memory by storing all rows when we can just store 2 rows using 2 1-D
            arrays.
            We will use dp and newDp of size (len(word2) + 1) and we set dp to newDp
            everytime we are done with current row.
            dp represents prev row
            newDp reprensents current row
            The only difference in logic is how we are going to access those 3 subcases.
        """
        dp = [index2 for index2 in range(len(word2) + 1)]

        for index1 in range(1, len(word1) + 1):
            newDp = [0] * (len(word2) + 1)
            newDp[0] = index1
            for index2 in range(1, len(word2) + 1):
                # EQUAL CASE:
                # We want dp[index1 - 1][index2 - 1] i.e; prev row, prev col So, dp[index2 - 1]
                if word1[index1 - 1] == word2[index2 - 1]: 
                    newDp[index2] = dp[index2 - 1]
                # UNEQUAL CASE:
                # a) we want dp[index1][index2 - 1] i.e; same row, prev col. So, newDp[index2 - 1]
                # b) we want dp[index1 - 1][index2] i.e; prev row, same col. So, dp[index2]
                # c) We want dp[index1 - 1][index2 - 1] i.e; prev row, prev col So, dp[index2 - 1]
                else:
                    newDp[index2] = min(
                        dp[index2], 
                        newDp[index2 - 1],
                        dp[index2 - 1]) + 1
            # Updating dp by setting current row as prev row for next iteration
            dp = newDp
        return dp[-1]
