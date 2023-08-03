######################################################

#   Solved on Saturday, 05 - 03 - 2022.

######################################################


######################################################

#   Runtime: 104ms   -   100.00%
#   Memory: 14.2MB  -   69.66%

######################################################

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        answer = [0] * len(nums)
        
        for i in range(len(nums)):
            answer[i] = nums[nums[i]]
        
        return answer