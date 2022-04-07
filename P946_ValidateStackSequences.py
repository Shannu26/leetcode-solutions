######################################################

#   Solved on Wednesday, 16 - 03 - 2022.

######################################################


######################################################

#   Runtime: 85ms   -   72.25%
#   Memory: 14.1MB  -   93.97%

######################################################

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        # Initialsing stack with first pushed item
        stack = [pushed[0]]
        # Since we already pushed first item present at index 0, initialsing pushIndex
        # with 1
        pushIndex = 1
        popIndex = 0
        # Looping through pushed stack
        while pushIndex < len(pushed):
            # If stack is empty there is no chance of popping an element
            # So, we append next pushed item into stack
            if not stack: 
                stack.append(pushed[pushIndex])
                pushIndex += 1
            # If stack is not empty and top of the stack is equal to next popped item,
            # now is the time to pop it from stack. Because later we won't be able to
            # pop it since we add new items to stack.
            elif popped[popIndex] == stack[-1]:
                stack.pop()
                popIndex += 1
            # If stack is not empty and also top doesn't match with next popped item
            # we add it to stack
            else:
                stack.append(pushed[pushIndex])
                pushIndex += 1
        # After above loop is done, there are 2 possibilities
        # Either popIndex also reached len(popped) which means stack became empty
        # or there are still some elements in stack and popIndex hasn't reached len(popped)
        # So, we pop the remaining elements if top of stack matches next popped item
        while popIndex < len(popped):
            # If top doesn't match next popped item, there is no way we can empty
            # the stack by using these pushed and popped stack since pushed stack
            # is already done. So we return False
            if popped[popIndex] != stack[-1]: return False
            # Else, we pop from stack
            stack.pop()
            popIndex += 1
        # We reach here only if given pushed and popped sequences are valid. So we
        # return True
        return True