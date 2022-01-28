######################################################

#   Solved on Wednesday, 08 - 09 - 2021.

######################################################


######################################################

#   Runtime: 24ms   -   95.04%
#   Memory: 13.9MB  -   98.93%

######################################################

class Solution:
    def decodeString(self, s: str) -> str:
        
        stack = []
        # Added these to the string just to have a linear exection path
        s = "1[" + s + "]"
        i = 0
        while i < len(s):
            # If we encounter ] we have to get get the string of chars from
            # stack till we encounter [
            # Then we again pop from stack to get number of times that string
            # has to repeat and we multiply that string with that number
            # and we again add it to stack
            if s[i] == "]":
                substring = ""
                while stack[-1] != "[":
                    # Removing Alphabets
                    substring = stack.pop() + substring
                # Removing [
                stack.pop()
                # Removing number from stack and adding substring * number to
                # stack
                stack.append(substring * int(stack.pop()))
            # If we encounter a number, we loop till we encounter [ and then we add
            # that number string to stack
            elif 47 < ord(s[i]) < 58:
                num = ""
                while 47 < ord(s[i]) < 58: 
                    num += s[i]
                    i += 1
                i -= 1
                stack.append(num)
            # If we encounter anything other than numbers or ] i.e; alphabets or [ we 
            # directly add it to stack
            else: stack.append(s[i])
            
            i += 1
        return stack[0]