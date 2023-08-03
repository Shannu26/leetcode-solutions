######################################################

#   Solved on Friday, 10 - 12 - 2021.

######################################################


######################################################

#   Runtime: 28ms   -   96.14%
#   Memory: 14.4MB  -   97.13%

######################################################

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Result array to store all the possible parenthesis
        parenthesis = []
        def backtrack(string = "", left = 0, right = 0):
            """
                This method will use backtracking paradigm to generate all possible
                valid parenthesis
                Parameters:
                    string - The current parenthesis string
                    left - Number of open brackets in string
                    right - Number of close brackets in string
            """
            # This is the base case required for our backtracking method. We will
            # go only the paths which will result in valid parenthesis. So, a valid
            # parenthesis having n pairs of parenthesis will have a size of 2 * n.
            # So, if we get the string of len == 2 * n, we will add it to result array
            if len(string) == 2 * n:
                parenthesis.append(string)
                return
            # A valid parenthesis of size n, should not have opening brackets > n.
            # So, we go in the path of string + "(" only if number of open brackets
            # < n.
            if left < n:
                backtrack(string + "(", left+1, right)
            # A valid parenthesis can't have more number of close brackets than open
            # brackets. So, we go in the path of string + ")" only if number of close
            # brackets < number of open brackets
            if right < left:
                backtrack(string + ")", left, right+1)
        backtrack()
        return parenthesis