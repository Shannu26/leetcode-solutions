######################################################

#   Solved on Wednesday, 16 - 03 - 2022.

######################################################


######################################################

#   Runtime: 32ms   -   83.79%
#   Memory: 13.7MB  -   99.39%

######################################################

class Solution:
    def addDigits(self, num: int) -> int:
        # The divisibility rule of 9 is, if sum of all the digits in a given num1
        # is divisible by 9, then that numb1 is divisible by 9. If we think
        # the num2 we get after adding the digits of num1 is divisible by 9 only if
        # sum of digits of num2 is divisible by 9. We can repeat this process till
        # we get to a single digit and understand that a num is divisible by 9
        # if sum of digits recursively gives us 9.
        # Example: 123456789
        #          1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9
        #          45
        #          4 + 5
        #          9
        # So, 123456789 is divisible by 9
        # If a number is not divisible by 9, we get sum of digits recursively not 9
        # Example: 123456788
        #          1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 8
        #          44
        #          4 + 4
        #          8
        # So, 123456788 is not divisible by 9
        # If we try to divide number by 9, the possible remainders are 0 to 8
        # From that what we can understand is, if we get a remainder 0, num is divisible
        # by 9
        # If we get remainder 2 that means sum of all digits is 2 and so on

        # If num is 0, sum will be 0
        if num == 0: return 0
        # If num is divisible by 9, sum is 9
        if num % 9 == 0: return 9
        # Else, sum will be the remainder of num % 9
        return num % 9