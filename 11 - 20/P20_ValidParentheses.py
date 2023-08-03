######################################################

#   Solved on Monday, 12 - 07 - 2021.

######################################################


######################################################

#   Runtime: 24ms   -   95.98%
#   Memory: 14.1MB  -   86.14%

######################################################

class Solution:
    def isValid(self, s: str) -> bool:
        
        # To push opening chars into top of tack
        stack = []
        
        for i in s:
            
            # If current char is opening char, push it into stack
            if i in {"{", "(", "["}:
                stack.append(i)

            # If current char is closing char
            else:
                # If stack is empty, that means there is no opening char for this 
                # closing char. so return false
                if not stack: return False

                # Getting the top char from stack
                char = stack.pop()

                # Checking whether current closing char matches with the corresponding
                # opening char present in top of stack. If not return false
                if i == "}":
                    if char != "{": return False
                
                if i == ")":
                    if char != "(": return False
                
                if i == "]":
                    if char != "[": return False
        
        # If stack still has some opening chars in it, that means there are some
        # Opening chars with no closing chars for them. so return false if len(stack)
        # != 0, else true
        return len(stack) == 0