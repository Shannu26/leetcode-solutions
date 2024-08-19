######################################################

#   Solved on Monday, 11 - 06 - 2023.

######################################################


######################################################

#   Runtime: 52ms   -   93.84%
#   Memory: 17.96MB  -  100.00%

######################################################

class MinStack:

    def __init__(self):
        self.stack = []
        self.minValue = [math.inf]

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.minValue.append(min(val, self.minValue[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.minValue.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minValue[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()