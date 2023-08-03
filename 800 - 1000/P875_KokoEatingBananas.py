######################################################

#   Solved on Tuesday, 25 - 01 - 2022.

######################################################


######################################################

#   Runtime: 459ms   -   86.64%
#   Memory: 15.5MB  -   87.85%

######################################################

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def isPossible(k):
            """
                This function will find the hours required for koko to eat all
                bananas at k banana per hour
                Then we will check whehter number of hours required <= h and return
                the resultant boolean
            """
            numOfHours = 0
            for pile in piles:
                # if pile = 10 and k = 3, numOfHours will be 4 since it takes 3 hours
                # to eat 9 bananas and in 4th hour it will eat remaining 1 banana and
                # sit idle to complete that 4th hour
                # This line will give the quotient which is 3
                numOfHours += pile // k
                # If we have remainder, that means there are still banans left after
                # quotient hours. So, it will take 1 hour more to eat them. So increase
                # numOfHours by 1 to make 4 for above example
                if pile % k: numOfHours += 1
                # This condition will help in avoiding unnecessary traversal of entire
                # array if numOfHours required to eat bananas from 0 pile to current
                # pile exceeded h. If yes, it is not possible to complete all bananas
                # at k banana per hour. So we return False
                if numOfHours > h: return False
            # We will reach here only if after considering last pile, numOfHours
            # haven't exceeded h. So we return True
            return True
        
        # Binary Search Starts
        low = 1
        high = max(piles)
        
        while low < high:
            k = (low + high) // 2
            # If eating k bananas per hour is possible, we can say that
            # Either it will be required k or required k will be < current k
            # But min K won't be > this k right. So, we set upper limit to k
            if isPossible(k): high = k
            # If If eating k bananas per hour is not possible, we can say that
            # eating bananas < k will also won't be possible. So we set lower limit
            # to k + 1
            else: low = k + 1
        # loop will end when low == high. So, we min will be low or high. So we return
        # it
        return low