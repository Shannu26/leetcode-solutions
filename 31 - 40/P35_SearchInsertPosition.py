######################################################

#   Solved on Saturday, 01 - 01 - 2022.

######################################################


######################################################

#   Runtime: 40ms   -   97.99%
#   Memory: 14.8MB  -   94.36%

######################################################

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Logic is to do Binary Search

        start = 0
        end = len(nums) - 1
        
        while start <= end:
            mid = ( start + end ) // 2
            # If given element is present return that index which is stored in mid
            if nums[mid] == target: return mid
            # If nums[mid] > target, since array is sorted we can't find target to
            # right of mid. So changing end to mid - 1 
            elif nums[mid] > target: end = mid - 1
            # If nums[mid] < target, since array is sorted we can't find target to 
            # left of mid. So changing start to mid + 1
            else: start = mid + 1
        # If target not found, return start index which will be the index at which
        # this target fits.        
        return start