######################################################

#   Solved on Friday, 03 - 09 - 2021.

######################################################


######################################################

#   Naive Approach

#   Time Limit Exceeded
#   77 / 80 Test cases passes

######################################################

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        if len(needle) == 0: return 0
        if len(haystack) == 0: return -1
        if len(needle) > len(haystack): return -1
        
        # The logic is to loop through each index i of haystack string and checking
        # if needle is a substring starting from i. If yes we return i
        for i in range(len(haystack)):
            for j in range(len(needle)):
                if (j + i) == len(haystack) or haystack[i + j] != needle[j]: break
            else: return i
        
        return -1

######################################################

#   Improved Naive Approach

#   Runtime: 40ms   -   67.04%
#   Memory: 14.4MB  -   60.91%

######################################################

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        if len(needle) == 0: return 0
        if len(haystack) == 0: return -1
        if len(needle) > len(haystack): return -1
        
        # The logic is similar to above approach with a very slight improvement. 
        # Instead of only checking chars of needle from left to right, we simultaneously
        # check left to right and right to left so that we can avoid strings which
        # match with needle from start and not match near the end.
        for i in range(len(haystack)):
            start = 0
            # We set end to -1 if len(needle) + i exceeds the len(haystack).
            # Why because, we anyways can't find that needle in substring starting
            # from i, since haystack doesn't have required number of chars for needle
            end = len(needle) - 1 if len(needle) - 1 + i < len(haystack) else -1
            if end == -1: break
            while start <= end:
                # Checking left char
                if haystack[start + i] != needle[start]: break
                # Checking right char
                if haystack[end + i] != needle[end]: break
                start += 1
                end -= 1
            else: return i
        
        return -1