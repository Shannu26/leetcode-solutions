######################################################

#   Solved on Monday, 24 - 01 - 2022.

######################################################


######################################################

#   Runtime: 36ms   -   83.30%
#   Memory: 14MB  -   98.62%

######################################################

class Solution:
    def secondHighest(self, s: str) -> int:
        
        first = -1
        second = -1
        
        for char in s:
            # If char is a digit
            if 48 <= ord(char) <= 57:
                # Storing the value of digit
                value = ord(char) - 48
                # Since problem requires second largest. if current digit == first
                # largest digit no need to do anything so we skip loop
                if value == first: continue
                # If current digit > first largest digit we transfer first to second
                # and store value in first
                if value > first:
                    second = first
                    first = value
                # If current digit < first and > second we store value in second
                elif value > second:
                    second = value
        
        return second