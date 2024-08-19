######################################################

#   Solved on Monday, 08 - 19 - 2024.

######################################################


######################################################

#   Runtime: 27ms   -   97.95%
#   Memory: 16.50MB  -   88.15%

######################################################

class Solution:
    def minSteps(self, n: int) -> int:
        """
            The logic is to greedily select which direction we
            want to go at each possible decision tree.
            We have 2 directions possible.
            1) Using the previous copy value and paste it to get
            currentValue + prevCopyValue with numOfSteps increased by 1
            2) Copying and pasting current value to get 2 * currentValue
            with numOfSteps increased by 2
            If you observe the attached image, we can see that to get min
            number of steps, if n % currentValue == 0, we can take the direction
            2 since currentValue is a factor of n, we can just keep on multiplying
            the same copy value to eventually get n.
            If n % currentValue != 0, we can't take direction 2 since it will lead
            us to a dead end for sure. So, we take direction 1.
            We repeat this process till we reach n.
            It is hard to visualize. I was able to figure it out once I drew the 
            decision tree first.
        """
        # Initially we have only 1 'A', we didn't copy anything so it is ''
        currentValue, prevCopyValue, numOfSteps = 1, 0, 0

        while currentValue != n:
            # Direction 2
            if n % currentValue == 0:
                # Copied currentValue, then pasted it
                prevCopyValue = currentValue
                currentValue = 2 * currentValue
                numOfSteps += 2
            # Direction 1
            else:
                # Pasted already copied value
                currentValue += prevCopyValue
                numOfSteps += 1
        
        return numOfSteps