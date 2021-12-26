######################################################

#   Solved on Tuesday, 24 - 08 - 2021.

######################################################


######################################################

#   Runtime: 36ms   -   97.62%
#   Memory: 14.2MB  -   84.10%

######################################################

class Solution:
    def romanToInt(self, s: str) -> int:
        
        num = 0
        # At every index i, prevValue will have value of (i+1)th index. Since we 
        # begin at end and there will be no value to its right, we initialize with 0
        prevValue = 0
        
        charsDict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        # Looping through the string from backwards
        for i in range(len(s) - 1, -1, -1):
            # Getting value of current index
            curValue = charsDict[s[i]]
            # If curValue < prevValue, then we have encountered a case in the possible
            # 6 instances where we have to subtract the value of current index. So
            # we do num -= curValue. Else we add it by num += curValue
            if curValue < prevValue:
                num -= curValue
            else: num += curValue
            # changing prevValue to curValue since in next iteration curValue will
            # be its prevValue
            prevValue = curValue
        
        return num