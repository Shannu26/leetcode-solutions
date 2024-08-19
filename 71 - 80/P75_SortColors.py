######################################################

#   Solved on Thursday, 02 - 01 - 2024.

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

        # To track next index to set to 0
        zerosIndex = 0
        # To track next index to set to 2
        twosIndex = len(nums) - 1

        index = 0
        while index <= twosIndex:
            # If value is 2, we swap it with value at twosIndex
            if nums[index] == 2:
                nums[index] = nums[twosIndex]
                nums[twosIndex] = 2
                # Updating twosIndex
                twosIndex -= 1
                # Since we don't know value at twosIndex
                # It might be 0 or 1 or 2. So we shouln't 
                # ignore it. So, not incrementing index
            # If value is 0, we swap it with value at zerosIndex
            elif nums[index] == 0:
                nums[index] = nums[zerosIndex]
                nums[zerosIndex] = 0
                # Updating zerosIndex
                zerosIndex += 1
                # Since we come from left to right, we already
                # know the value at zerosIndex since index is
                # always >= zerosIndex. So, we don't have to 
                # check its value again. So incrementing index
                index += 1
            # If value is 1, it should be in the middle only. So
            # incrementing index
            else: index += 1