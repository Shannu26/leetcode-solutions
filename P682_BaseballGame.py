######################################################

#   Solved on Sunday, 10 - 04 - 2022.

######################################################


######################################################

#   Runtime: 40ms   -   93.04%
#   Memory: 14MB  -   95.48%

######################################################

class Solution:
    def calPoints(self, ops: List[str]) -> int:
        
        stack = []
        
        for op in ops:
            if op == "C": 
                stack.pop()
            elif op == "+":
                stack.append(stack[-1] + stack[-2])
            elif op == "D":
                stack.append(stack[-1] * 2)
            else:
                stack.append(int(op))

        return sum(stack)