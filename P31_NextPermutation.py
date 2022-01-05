######################################################

#   Solved on Saturday, 01 - 01 - 2022.

######################################################


######################################################

#   Runtime: 36ms   -   93.50%
#   Memory: 14MB  -   99.37%

######################################################

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
            Do not return anything, modify nums in-place instead.
        """
        
        i = len(nums) - 2
        
        while i > -1 and nums[i] >= nums[i + 1]: i -= 1

        if i > - 1:
            j = len(nums) - 1
            while nums[j] <= nums[i]: j -= 1
                
            nums[j], nums[i] = nums[i], nums[j]
        
        start = i + 1
        end = len(nums) - 1
        
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1