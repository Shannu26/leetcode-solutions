######################################################

#   Solved on Monday, 30 - 08 - 2021.

######################################################


######################################################

#   Runtime: 103ms   -   94.17%
#   Memory: 14.1MB  -   98.11%

######################################################

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        nums.sort()
        result = float('inf')
        # startIndex will be the first index of a pair of 3 indices for each iteration
        for startIndex in range(len(nums)):
            # This will help us to eliminate redundant calculations. Becasue if
            # nums[i] == nums[i - 1] the values that are possible by using nums[i]
            # are already calculated in (i-1)th iteration
            if startIndex != 0 and nums[startIndex] == nums[startIndex - 1]: continue
            ##### Two Sum Logic begins here. Only difference is a single if condition
            ##### to update result var

            # First pointer
            i = startIndex + 1
            # Second pointer
            j = len(nums) - 1
            while i < j:
                curSum = nums[i] + nums[j] + nums[startIndex]
                # Why we return is, since given numbers are integers, the closest
                # sum to target that is possible is target itself, since they have a
                # differene of 0. So it is a waste of time complexity if we still 
                # continue if we encountered a sum = target
                if curSum == target: return target
                # This is the if condition which is different from actual twoSum problem
                # If the curSum is more closer to target than already encountered result
                # We update the result
                if abs(result - target) > abs(curSum - target):
                    result = curSum
                if curSum > target: j -= 1
                else: i += 1
        
        return result