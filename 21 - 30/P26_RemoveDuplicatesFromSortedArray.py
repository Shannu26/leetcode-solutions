######################################################

#   Solved on Thursday, 12 - 08 - 2021.

######################################################


######################################################

#   Runtime: 80ms   -   88.96%
#   Memory: 15.4MB  -   96.37%

######################################################

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # This var is a pointer to a index which will be the first instance of a
        # val.
        index = 0
        # We loop from 1 to end of nums and check if nums[i] != nums[index], then that
        # means we got next first instance of a val. So we increment index by 1
        # and store in that index nums[i] val
        for i in range(1, len(nums)):
            if nums[i] != nums[index]:
                index += 1
                nums[index] = nums[i]
        # Return index + 1, since index starts from 0 and the question asked for
        # after k positions, not k indexes. 
        return index + 1