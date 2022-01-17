######################################################

#   Solved on Sunday, 16 - 01 - 2022.

######################################################


######################################################

#   Runtime: 24ms   -   97.39%
#   Memory: 13.9MB  -   98.77%

######################################################

class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        
        if n == 0: return 0
        # Initializing the array
        nums = []
        nums.append(0)
        nums.append(1)
        maxValue = 1
        # Generating the array with the given logic and updating the maxValue,
        # if generated new value > maxValue
        for i in range(2, n + 1):
            # Since adding nums[i] is common for both nums[2 * i] and nums[2 * i + 1]
            # We are directly appending nums[i // 2] into array for index i
            nums.append(nums[i // 2])
            # Then if i is odd, we are updating last value of array with
            # nums[i // 2 + 1] too
            if i % 2 != 0: nums[-1] += nums[i // 2 + 1]
            # Updating max value
            maxValue = max(maxValue, nums[i])
        
        return maxValue