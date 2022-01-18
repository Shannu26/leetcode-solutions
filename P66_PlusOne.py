######################################################

#   Solved on Thursday, 28 - 10 - 2021.

######################################################


######################################################

#   Runtime: 28ms   -   92.61%
#   Memory: 14.1MB  -   91.98%

######################################################

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        carry = 1
        index = -1
        # index + len(digits) will be -1 only when index becomes -1 * (len(digits) + 1)
        # It will happen only when adding 1 to the number in the digits exceeded
        # the length. Example, digits = [9, 9, 9] and adding 1 makes it [1, 0, 0, 0]
        while carry and index + len(digits) != -1:
            # Loops till there is a carry present and index didn't exceed the length
            # of digits list

            # Adds 1 to digit in index position
            digits[index] += 1
            # Getting the 10's place of digits[index] which will 0 if it is < 10, else
            # it will be 1
            carry = digits[index] // 10
            # Getting the 1's place of digits[index]
            digits[index] %= 10
            # Decrementing index to go to next index from the end of the array.
            index -= 1
        
        # If we still have carry, that means adding 1 to the digits exceeded the 
        # length of the digits. So we insert 1 at the beginning of the list
        if carry: digits.insert(0, 1)
        
        return digits