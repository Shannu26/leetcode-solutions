######################################################

#   Solved on Saturday, 23 - 10 - 2021.

######################################################


######################################################

#   Runtime: 28ms   -   93.91%
#   Memory: 14MB  -   98.70%

######################################################

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
            Logic is, we loop through the array and do 2 things
            1. If nums[i] == 0, we place it at the index pointer which tells us the
            next index in which we have to place 0
            2. If nums[i] == 2, we increase twoCount var

            In general words, in the first loop we will put all 0's in the front
            and we also find number of 2's in the array

            In next loop, we loop starting from 'index' position since before index
            all will 0's. In the loop, if array has k 2's, last k elements in the array
            should be zero. So if i < len(nums) - k we put 1 in nums[i] else we put 2
        """

        # Variable to store number of 2's in array
        twoCount = 0
        # index represents the current pointer in the array in which we will place 0
        index = 0
        # Placing 0's in the beginning and finding 2's count
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[index] = 0
                index += 1
            if nums[i] == 2:
                twoCount += 1
        # Placing 1's and 2's in the arrray
        for i in range(index, len(nums)):
            if i < len(nums) - twoCount: nums[i] = 1
            else: nums[i] = 2