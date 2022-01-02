######################################################

#   Solved on Sunday, 02 - 01 - 2022.

######################################################


######################################################

#   Linear Search Approach

#   Runtime: 32ms   -   97.86%
#   Memory: 14.6MB  -   78.9%

######################################################


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        for i in range(len(nums)):
            if nums[i] == target: return i
        
        return -1


######################################################

#   Binary Search Approach - I

#   Runtime: 36ms   -   91.75%
#   Memory: 14.5MB  -   92.86%

######################################################


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        i = 1
        # Finding the pivot index by finding when nums[i] < nums[i - 1]
        while i < len(nums) and nums[i] > nums[i - 1]: i += 1
        
        # Doing binary search on left subarray and right subarray from pivot index
        l = Solution.binarySearch(nums[:i], target)
        h = Solution.binarySearch(nums[i:], target)
        
        # if l != -1 then required element is in left subarray and we return the found
        # index
        if l != -1: return l
        # if h != -1 then required element is in right subarray and we return the found
        # index + the starting index of the subarray which is pivot index
        if h != -1: return h + i
        # if both l and h are -1 then target is not in the array
        return -1
    
    def binarySearch(nums, target):
        print(nums)
        
        l = 0
        h = len(nums) - 1
        
        while l <= h:
            m = (l + h) // 2
            
            if nums[m] > target: h = m - 1
            elif nums[m] < target: l = m + 1
            else: return m
        
        return -1

######################################################

#   Binary Search Approach - II

#   Runtime: 36ms   -   91.38%
#   Memory: 14.5MB  -   92.86%

######################################################


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if  nums[mid] == target: return mid
            # If nums[mid] >= nums[left] then subarray from left to mid is in 
            # ascending sorted order
            if  nums[mid] >= nums[left]:
                # So, if target is >= nums[left] and < nums[mid], it might lie only
                # between left and mid indices. So, we change, right to mid - 1
                if nums[left] <= target < nums[mid]: right = mid - 1
                # Else, it might lie only between mid + 1 and right indices. So, we
                # change left to mid + 1
                else: left = mid + 1
            # If nums[mid] < nums[left], then subarray from mid to right is in sorted
            # order.
            else:
                # So, if target > nums[mid] and <= nums[right], it might lie only 
                # between mid + 1 and right indices. So, we change left to mid + 1
                if nums[mid] < target <= nums[right]: left = mid + 1
                # Else, it might lie only between left and mid - 1 indices. So, we 
                # change, right to mid - 1
                else: right = mid - 1
        
        return -1