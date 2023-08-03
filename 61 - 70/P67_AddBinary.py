######################################################

#   Solved on Wednesday, 19 - 01 - 2022.

######################################################


######################################################

#   Runtime: 28ms   -   95.30%
#   Memory: 14.1MB  -   79.14%

######################################################


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        index = -1
        carry = 0
        result = ""
        # Looping till either of strings have chars left
        while index >= -len(a) or index >= -len(b):
            # Initializing total with carry we got from previous iteration
            total = carry
            # If a has still chars left, we get int value at index and add it to total
            if index >= -len(a): total += int(a[index])
            # If b has still chars left, we get int value at index and add it to total
            if index >= -len(b): total += int(b[index])
            # Total will have values of either
            # 0 - if carry and a[index] and b[index] == 0
            # 1 - if only one of carry and a[index] and b[index] == 1
            # 2 - if 2 of carry and a[index] and b[index] == 1
            # 3 - if carry and a[index] and b[index] == 1
            # In binary these are 00, 01, 10, 11
            # To get the Least significant bit we need to divide them by 2 and take
            # the remainder.
            # We take it and add it to result
            result = str(total % 2) + result
            # To get most significant bit which will be next carry, we need to divide
            # by 2 and take the quotient
            carry = total // 2
            index -= 1
        # If we still have a carry, then we add 1 at start of result
        if carry: return "1" + result
        return result