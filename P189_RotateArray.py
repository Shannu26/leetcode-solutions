######################################################

#   Solved on Tuesday, 01 - 02 - 2022.

######################################################


######################################################

#   Approach 1: Using O(n) extra space

#   Runtime: 212ms   -   90.39%
#   Memory: 25.4MB  -   96.40%

######################################################

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # If we rotate nums len(nums) times we will again get the original
        # array. So if k > len(nums) we just have to rotate k % len(nums)
        k = k % len(nums)
        # Creating copy of nums array
        nums_copy = nums[:]
        # Modifying nums array
        for i in range(len(nums)):
            # Placing at nums[i] value at i-k position. Because if we rotate
            # value at index i, k number of times it will go to (i+k) index
            # So we can say that at nums[i] we will have nums[i-k] value
            # We can easily do this in python since it supports -ve indexing
            # Because of that at nums[0], for k = 2, we will place value at
            # nums[-2]. In other languages if we want to do this, we might need
            # code like
            # if i - k < 0:
            #   nums[i] = nums_copy[len(nums) - k + i]
            # else: nums[i] = nums_copy[i - k]
            nums[i] = nums_copy[i - k]

######################################################

#   Approach 2: Using O(1) extra space

#   Runtime: 224ms   -   75.75%
#   Memory: 25MB  -   99.46%

######################################################

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # If we rotate nums len(nums) times we will again get the original
        # array. So if k > len(nums) we just have to rotate k % len(nums)
        k = k % len(nums)
        # Logic is, if we observe the input and output we will understand that
        # after moving k times to the right, last k elements will come to the 
        # start of the array and they will be in their order just as before
        # If we want to do it using O(1) we have to figure out a way to bring
        # last k values to the start.
        # One thing we can do is, we can reverse the array. In that way
        # last k elements will come to first. But they will be in reverse order right
        # So, next we will reverse the first k elements. Now, first k elements are 
        # in correct order. But the elements after k are still in reverse order
        # So, we reverse them.
        # It is slower than above solution clearly. But it satisfies the given
        # follow up challenge to solve in O(1) space

        # Reversing entire array
        for i in range(len(nums) // 2):
            nums[i], nums[-(i + 1)] = nums[-(i + 1)], nums[i]
        # Reversing first k elements
        for i in range(k // 2):
            nums[i], nums[k - i - 1] = nums[k - i - 1], nums[i]
        # Reversing elements from k index to last
        for i in range(k, (len(nums) - k) // 2 + k):
            nums[i], nums[len(nums) - i - 1 + k] = nums[len(nums) - i - 1 + k], nums[i]