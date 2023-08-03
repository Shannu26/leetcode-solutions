######################################################

#   Solved on Saturday, 07 - 08 - 2021.

######################################################


######################################################

#   Runtime: 27ms   -   88.63%
#   Memory: 13.9MB  -   99.91%

######################################################

class Solution:
    def reverse(self, x: int) -> int:
        
        if x == 0: return 0
        
        # Used to determine whether after reversing we should multiply by -1 or 1
        multiplier = 1
        # If x i -ve number, multiply by -1 to make it +ve and set multiplier to -1
        if x < 0:
            x = x * -1
            multiplier = -1
        
        reverse = 0
        
        while x != 0:
            # Getting the last digit
            r = x % 10
            x = x // 10
            # If current value of reverse is 214748364 and if given num if a +ve num
            # then the max limit for it is 2147483647. So we are checking if 
            # reverse = 214748364 and mulitplier == 1 and r > 7, which would make 
            # reverse pass the upper bound of integer range. If yes, we return 0
            if reverse == 214748364 and r > 7 and mulitplier == 1: return 0
            # If current value of reverse is 214748364 and if given num if a -ve num
            # then the max limit for it is -2147483648. So we are checking if 
            # reverse = 214748364 and mulitplier == -1 and r > 8, which would make 
            # reverse pass the lower bound of integer range. If yes, we return 0
            if reverse == 214748364 and r > 8 and mulitplier == -1: return 0
            # If current value of reverse if > 214748364, then adding any more digit
            # will make it pass boundary of integer range. So we return 0
            if reverse > 214748364: return 0
            # Adding current digit to reverse
            reverse = reverse * 10 + r
        return reverse * multiplier