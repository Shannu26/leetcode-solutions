######################################################

#   Solved on Friday, 25 - 06 - 2021.

######################################################


######################################################

#   Runtime: 28ms   -   94.32%
#   Memory: 14.1MB  -   93.88%

######################################################
class Solution:
    def myAtoi(self, s: str) -> int:
        
        result = 0
        # To determine the sign of the result
        sign = 1
        
        i = 0
        
        # Ignoring whitespaces
        while i < len(s) and s[i] == " ": i += 1
        
        # Checking if the string is an empty string with only white spaces
        if i == len(s): return 0
        
        # Determining the sign of number
        if s[i] == "-" or s[i] == "+":
            if s[i] == "-": sign = -1
            
            i += 1
        
        # Determining the number till we reach end of string or we encounter a 
        # charaacter other than numbers
        while i < len(s) and ord(s[i]) >= 48 and ord(s[i]) <= 57:
            result = result * 10 + int(s[i])
            i += 1
            
            # Checking if result exceeeded -2^31
            if result * sign <= -2147483648:
                return -2147483648
            
            # Checking if result exceeded 2^31 - 1
            if result * sign >= 2147483647:
                return 2147483647
        
        # Returning the resulting with correct sign
        return result * sign