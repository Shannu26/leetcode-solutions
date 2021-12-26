######################################################

#   Solved on Saturday, 28 - 08 - 2021.

######################################################


######################################################

#   Runtime: 48ms   -   95.13%
#   Memory: 14.1MB  -   77.39%

######################################################

class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
            The logic is, instead of reversing x which might lead to integer
            range overflow, what we can do is, if the number is a palindrome 
            reverse of half of the digits will be equal to remaining half if
            number is of even length. Otherwise, a part from the middle digit
            reverse of digits to left of middle digit will be equal to digits
            to the right of middle digit.
            Example 1: 1221 -> "12" + "21"
                    Reverse of first half digits is 21 which is equal to second
                    half digits.
            Example 2: 121 -> "1" + "21"
                    Reverse of first half of digirs is 1 which is equal to second
                    half digits excluding middle digit(2).
        """

        # -ve numbers and numbers other than 0 which have 0 as last digit won't be
        # palindrome
        if x < 0 or (x % 10 == 0 and x != 0): return False
        
        xReverse = 0
        # When xReverse becomes > x, that means we successfully reverse half digits
        while x > xReverse:
            lastDigit = x % 10
            x = x // 10
            
            xReverse = xReverse * 10 + lastDigit
        # For even length x, x is palindrome if x == xReverse
        # For odd length x, x is palindrome if xReverse // 10 which will give number
        # excluding middle digit == x
        return xReverse == x or xReverse // 10 == x