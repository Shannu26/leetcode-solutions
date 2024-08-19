######################################################

#   Solved on Wednesday, 11 - 08 - 2021.

######################################################


######################################################

#   Runtime: 1034ms   -   86.84%
#   Memory: 29.11MB  -   99.68%

######################################################

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
            The logic is to make use of monotonic stack.
            A monotonic stack stores values only in increasing order or
            decreasing order.
            But, in our problem we are using monotonic stack to store 
            indexes of temperatures where temperatures[index] follow the
            monotonic stack property.
            We are using monotonic stack which stores values in increasing order
            i.e; top of the stack has the minimum value.

            The logic is we loop through the temperatures array in reverse order
            and since we want to find next temperature which is > current day 
            temperature, we repeatedly pop values from stack which have temperature
            <= current temperature. This loop ends when stack is empty or when
            current temperature > temperature of top of stack. That means we have found
            our next highest temperature. So, we store that in waitDays array.
            If we are at index i and top of stack with next max is j, number of days
            is j - i right. So, we do waitDays[i] = j - i (where j = stack[-1])
            We add our index to stack.
        """
        waitDays = [0] * len(temperatures)
        monotonicStack = []

        for index in range(len(temperatures) - 1, -1, -1):
            while monotonicStack and temperatures[monotonicStack[-1]] <= temperatures[index]: 
                monotonicStack.pop()

            if monotonicStack: waitDays[index] = monotonicStack[-1] - index
            monotonicStack.append(index)
        
        return waitDays