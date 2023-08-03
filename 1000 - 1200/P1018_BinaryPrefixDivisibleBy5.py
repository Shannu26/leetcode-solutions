######################################################

#   Solved on Thursday, 14 - 04 - 2022.

######################################################


######################################################

#   Runtime: 358ms   -   73.84%
#   Memory: 15.1MB  -   85.01%

######################################################

class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        
        number = 0
        isDivisible = [False] * len(nums)
        
        for index in range(len(nums)):
            # Since we need to add current bit at right of number, moving bits of number
            # to left by 1, adding 0 at right most bit. It is similar to 
            # number = number * 2
            number = number << 1
            # Adding current bit val to right bit
            number += nums[index]
            # Checking if number is divisible by 5 and updating the isDivisible[index]
            isDivisible[index] = not number % 5
        
        return isDivisible