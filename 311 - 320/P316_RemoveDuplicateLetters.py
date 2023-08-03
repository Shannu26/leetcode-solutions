######################################################

#   Solved on Friday, 18 - 03 - 2022.

######################################################


######################################################

#   Runtime: 38ms   -   85.44%
#   Memory: 13.8MB  -   99.33%

######################################################

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        """
            Constraint we need to keep in mind is resultant string should be a
            subsequence of given string and lexographically smaller when compared
            to other possible strings

            We will take a stack to keep track of the visited chars
            We loop through string s
                If char is already visited we skip current iteration
                Else conditions we need to check are
                    a) stack has some elements. If not we can add our char into stack
                    b) current char < top of stack. If this is not true that means
                    current char is in lexographical order in the stack. So we can
                    add it to stack
                    c) top of stack element has instances to the right of current
                    char. If not, that means if we remove top element since it
                    doesn't match the lexographic order, then we can't again
                    add that char to stack later since it is not present. So, we 
                    have to leave it like that even if order is not maintained. So we 
                    can add it to stack
                If all these conditions are true, then top element doesn't match
                lexographic order and we have that char later in the string. We can
                add it in that moment. So, we remove this top element for now. Since
                we removed it, it is not visited right. So we consider it again as
                not visited
                We check these conditions as long as all these are met and remove
                top elements.
                When any of the condition fails, we add our current char to stack
                and set it as visited
            Finally, stack will have our required resulant string. So we join those
            chars and return it
        """
        # Storing lastIndex of chars
        lastIndex = [0] * 26
        for i in range(len(s)):
            lastIndex[ord(s[i]) - 97] = i
        
        visited = [False] * 26
        stack = []
        # Looping the string
        for i in range(len(s)):
            if visited[ord(s[i]) - 97]: continue
            # Checking the 3 conditions mentioned above
            while stack and s[i] < stack[-1] and i < lastIndex[ord(stack[-1]) - 97]: 
                # If all 3 are met, we remove top element and set it as not visited
                prev = stack.pop()
                visited[ord(prev) - 97] = False
            # Adding current char to stack and setting it visited
            stack.append(s[i])
            visited[ord(s[i]) - 97] = True  
        
        return "".join(stack)