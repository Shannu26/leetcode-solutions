######################################################

#   Solved on Tuesday, 13 - 07 - 2021.

######################################################


######################################################

#   Approach 1 - Using 2 arrays

#   Runtime: 244ms   -   56.22%
#   Memory: 21.7MB  -   33.67%

######################################################

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # left array stores product of elements left to the element at index i
        # right array stores product of elements right to the element at index i

        # We initialize the array with all 1 elements because, 0th index of left
        # array and -1th index of right array has no left and right elements. So 
        # we consider only right and left elements for them. so we start with 1.
        left = [1] * len(nums)
        right = [1] * len(nums)
        
        for i in range(1, len(nums)):
            
            # left[i-1] has prod of elements from 0 to i - 2. so to get left[i]
            # i.e; prod of elements from 0 to i - 1, it is enough to do 
            # left[i-1] * nums[i-1], since left[i-1] already has prod of 0 to
            # i - 2 elements
            left[i] = left[i - 1] * nums[i - 1]
            # right[-i] has prod of elements from -1 to -i + 1. so to get right[-i-1]
            # i.e; prod of elements from -1 to -i, it is enough to do 
            # right[-i] * nums[-i], since right[-i] already has prod of -1 to
            # -i + 1 elements
            right[-i - 1] = right[-i] * nums[-i]
        
        # Multiplying left and right products at every index to get requires prod
        # array and storing it in left array
        for i in range(len(nums)):
            left[i] = left[i] * right[i]
        
        return left


######################################################

#   Approach 2 - Using 1 array and 1 variable

#   Runtime: 220ms   -   98.60%
#   Memory: 20.9MB  -   98.41%

######################################################

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prod = [1] * len(nums)
        
        # Filling prod[i] with prod of elements from 0 to i - 1. Since prod[i - 1]
        # has prod from 0 to i - 2, it can be done just by prod[i - 1] * nums[i - 1]
        for i in range(1, len(nums)):
            prod[i] = prod[i - 1] * nums[i - 1]

        # Instead of array of prod of elements to right of i, it is sufficient, if we
        # we have prod of elements from i + 1 to end. Initializing with 1, since -1th
        # element has no right element
        reverseProd = 1
        
        for i in range(1, len(nums) + 1):
            # At any point -i, we will have prod of -i + 1 elements to end of array in
            # reverseProd var. So multiplying that to existing prod[-i] which will be
            # prod of elements from 0 to -i-1th element
            prod[-i] = prod[-i] * reverseProd
            # Updating reverseProd to next prod by multiplying with current element, 
            # Which we need in next iteration
            reverseProd *= nums[-i]
        
        return prod