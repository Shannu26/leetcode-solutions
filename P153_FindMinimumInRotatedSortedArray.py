######################################################

#   Solved on Monday, 25 - 10 - 2021.

######################################################


######################################################

#   Runtime: 32ms   -   98.50%
#   Memory: 14.3MB  -   95.06%

######################################################

class Solution:
    def findMin(self, nums: List[int]) -> int:
        # If array has only one element, return it
        if len(nums) == 1: return nums[0]
        # Since array is a rotated sorted array, we can be sure that nums[0] is the min
        # element if nums[0] < nums[-1]. Because, let's say nums = [1,2,3,4]. If it is
        # rotated 1 time, nums = [4,1,2,3]. nums[0] is not < nums[-1]. if it is 
        # rotated 2 times, nums = [3,4,1,2]. nums[0] is not < nums[-1] and so on.
        # So, nums[0] will be < nums[-1] only when the array becomes again sorted
        # after some number of times
        if nums[0] < nums[-1]: return nums[0]
        # Binary Search logic with a little modification
        front = 0
        last = len(nums) - 1
        
        while front <= last:
            mid = (front + last) // 2
            # Consider nums = [3,4,5,1,2]. and front = 0 and last = 4. Then mid will
            # be 2. We can see that nums[mid] > nums[mid + 1] only when nums[mid] is
            # the largest element of the array. So, we return nums[mid + 1] then,
            # since nums is rotated, smallest element will be next to largest element
            # to its right side
            if nums[mid] > nums[mid + 1]: return nums[mid + 1]
            # Consider nums = [4,5,1,2,3]. and front = 0 and last = 4. Then mid will
            # be 2. We can see that nums[mid-1] > nums[mid] only when nums[mid] is
            # the smallest element of the array. So, we return nums[mid] then,
            # since nums is rotated, smallest element will be next to largest element
            # to its right side
            if nums[mid - 1] > nums[mid]: return nums[mid]
            # If nums[mid] > nums[front], since it is a rotated sorted array, we can
            # be sure that elements between front and mid are not min elements. So,
            # we change front = mid + 1
            if nums[mid] > nums[front]: front = mid + 1
            # If nums[mid] < nums[front], since we already checked above whether 
            # nums[mid] is the smallest or not. We can clearly say that nums[mid] is
            # not smallest. So, smallest will be to left of mid only. So we change
            # last pointer to mid - 1
            else: last = mid - 1