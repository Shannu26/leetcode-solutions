######################################################

#   Solved on Saturday, 26 - 03 - 2022.

######################################################


######################################################

#   Runtime: 236ms   -   98.03%
#   Memory: 15.5MB  -   77.82%

######################################################

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        if target < nums[0] or target > nums[-1]: return -1
        
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            middle = (left + right) // 2
            
            if nums[middle] == target: return middle
            if nums[middle] > target: right = middle - 1
            else: left = middle + 1
        
        return -1