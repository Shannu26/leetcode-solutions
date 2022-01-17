######################################################

#   Solved on Sunday, 16 - 01 - 2022.

######################################################


######################################################

#   Runtime: 24ms   -   99.51%
#   Memory: 14.1MB  -   70.10%

######################################################

class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        """
            The logic is to use Greedy Approach.
            First we generate the fibonacci numbers <= k
            Then we start at the largest fibonacci number and while k is not 0
            we subtract fibonacci[i] from k if k > fibonacci[i] and increase
            count by 1.
        """
        fibonacciNumbers = [0, 1]
        # Generating fibonacci numbers
        while fibonacciNumbers[-1] < k:
            fibonacciNumbers.append(fibonacciNumbers[-1] + fibonacciNumbers[-2])
        # index starts at end of array
        index = -1
        minCount = 0

        while k != 0:
            # we can only use the number at index if it is < k.
            if k >= fibonacciNumbers[index]: 
                # Then we take that number into our bag and reduce that from k
                # So, we increase minCount by 1
                minCount += 1
                k -= fibonacciNumbers[index]
            index -= 1
        
        return minCount