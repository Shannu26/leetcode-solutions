######################################################

#   Solved on Thursday, 17 - 03 - 2022.

######################################################


######################################################

#   Runtime: 28ms   -   94.45%
#   Memory: 13.8MB  -   70.86%

######################################################

class Solution:
    def scoreOfParentheses(self, s: str) -> int:

        stack = []
        # Looping through string
        for char in s:
            # If char is "(" we add it to stack
            if char == "(":
                stack.append("(")
            else:
                # If char is ")", we pop out the top element from stack till
                # we find "(". The popped elements will be 2 * score of child
                # balanced parentheses of current closed parentheses we have found
                # So we will add them to score var
                score = 0
                while stack[-1] != "(":
                    score += stack.pop()
                # If score is 0, that means the top of stack is "(" and we have
                # () in the string. So we make score 1
                if score == 0: score = 1
                # We remove "(" from stack
                stack.pop()
                # We append twice the actual score that a balanced parentheses should
                # have into the stack
                stack.append( 2 * score)
        # stack will have only 1 element if s is of format "(A)"
        # Else it will have > 1 element.
        # Each element will be int of scores multiplied by 2.
        # We add them and divide by 2 to remove that extra multiple 2 which we have done
        # in our logic
        return sum(stack) // 2

        """
            Example: "(()())()"
            char        stack
             (            ["("]
             (            ["(", "("]
             )            ["(", 2]
             (            ["(", 2, "("]
             )            ["(", 2, 2]
             )            [8]
             (            [8, "("]
             )            [8, 2]

            Finally sum(stack) // 2
                    = (8 + 2) // 2
                    = 5
            which is the score of that string
        """