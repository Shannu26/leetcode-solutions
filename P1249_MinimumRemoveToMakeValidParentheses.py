######################################################

#   Solved on Tuesday, 15 - 03 - 2022.

######################################################


######################################################

#   Runtime: 120ms   -   78.30%
#   Memory: 15.1MB  -   99.65%

######################################################

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        stack = []
        # Looping throught the string
        for char in s:
            # Possible chars in string are "(" or ")" or lowercase english letter
            # If current char is ")"
            if char == ")":
                string = ""
                # We pop the top element from stack and concatenate value to string
                # till stack becomes empty or we find "("
                while stack and stack[-1] != "(":
                    string = stack.pop() + string
                # If stack is not empty, that means we break out of loop since we found
                # "(" at top of stack.
                # So, we pop "(" from stack and add "(" + string + ")"
                if stack: 
                    stack.pop()
                    stack.append("(" + string + ")")
                # If stack is empty, that means we haven't found a "(" for the
                # current ")". So we just append string to stack
                else: stack.append(string)
            # If char is "(" or alphabet we add it stack
            else: stack.append(char)
        
        validString = ""
        # Looping through the stack to concatenate all the vals in the stack to
        # generate resultant string
        for string in stack:
            # If string is "(" that means it has not supporting ")" in the given
            # string, so we don't add it to our result
            if string != "(": validString += string
        # Returning the string
        return validString