######################################################

#   Solved on Saturday, 26 - 06 - 2021.

######################################################


######################################################

#   Linear Search Approach

#   Runtime: 84ms   -   72.04%
#   Memory: 15.2MB  -   99.81%

######################################################

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        i = 0
        
        # Looping through the array till we find the left position of target element
        while i < len(nums) and nums[i] != target: i += 1
        
        # If i == len(nums), that means target element is not in array
        if i == len(nums): return [-1, -1]
        

        j = i
        i += 1
        
        # Looping through array till we find the right position of target element
        while i < len(nums) and nums[i] == target: i += 1
        
        return [j, i - 1]


######################################################

#   Binary Search Approach

#   Runtime: 76ms   -   97.08%
#   Memory: 15.2MB  -   99.81%

######################################################

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        if not nums: return [-1, -1]
        l = 0
        r = len(nums) - 1
        m = (l + r) / 2
        
        # Looping through array till we get the target element or l becomes > r
        while l <= r:
            m = (l + r) // 2
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else: break
        
        # if l > r that means we haven't found the target element
        if l > r: return [-1, -1]
        # Finding the left position of target element from m 
        i = m
        while i >= 0 and nums[i] == target: i -= 1
        # Finding the right position of target element from m
        j = m
        while j < len(nums) and nums[j] == target: j += 1
        
        return [i + 1, j - 1]
