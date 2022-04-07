######################################################

#   Solved on Saturday, 26 - 03 - 2022.

######################################################


######################################################

#   Runtime: 28ms   -   94.30%
#   Memory: 13.8MB  -   97.51%

######################################################

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # Logic is to use Binary Search

        # If version 1 is bad, then that is the first bad version right
        if isBadVersion(1): return 1
        # Left and right pointers
        left = 0
        right = n
        
        while left < right:
            # Finding mid point
            mid = (left + right) // 2
            # If mid version is bad, there are 2 possible cases
            # a) It is the first bad version. If yes, then mid-1 version will not be
            # bad right. So we check if mid-1 version is bad or not. If not bad, then
            # mid is the first bad version so, we return it
            # b) It is not the first bad version. If yes, first bad version is to
            # the left of it. So, we set right to mid - 1
            if isBadVersion(mid):
                # Case a)
                if not isBadVersion(mid - 1): return mid
                # Case b)
                right = mid - 1
            # If mid version is not bad, then all versions to the left of it will not
            # be bad right. So we set left to mid + 1
            else: left = mid + 1
        # We break out when left == right and we haven't yet found the first bad version
        # Then left or right version will be the first bad version
        return left