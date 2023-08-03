######################################################

#   Solved on Tuesday, 14 - 12 - 2021.

######################################################


######################################################

#   Runtime: 24ms   -   98.56%
#   Memory: 14MB  -   98.95%

######################################################

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Logic is we move all vals to the end of list.
        # lastIndex will point to the index from which all elements to its right will
        # be val only.
        # We initialise it with len(nums) - 1 at the start
        lastIndex = len(nums) - 1
        # index used to loop through list
        index = 0
        # We loop as long as index <= lastIndex. Because, elements to the right
        # of lastIndex will be val only
        while index <= lastIndex:
            # If nums[index] is val, we swap it with the element present at element
            # at nums[lastIndex]
            # We won't move index to its next position. Because there is a possibility
            # that element at lastIndex is val before placing val in it.
            if nums[index] == val:
                nums[index], nums[lastIndex] = nums[lastIndex], nums[index]
                # We move lastIndex one step to its left. Because, we already used
                # that spot to place a val from index position
                lastIndex -= 1
            # if nums[index] is not val, we increment index
            else: index += 1
        # Elements from index 0 to lastIndex won't have val. So we return lastIndex + 1
        # Why we return lastIndex + 1 is, lastIndex is 0 based and we need a value
        # based on 1 based because we need number of elements that are not val.    
        return lastIndex + 1