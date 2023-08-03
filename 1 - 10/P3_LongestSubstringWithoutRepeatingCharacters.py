######################################################

#   Solved on Sunday, 15 - 08 - 2021.

######################################################


######################################################

#   Space Optimal Solution

#   Runtime: 676ms   -   10.33%
#   Memory: 14.1MB  -   99.16%

######################################################

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        globalLen = 0
        i = 0
        
        while i < len(s):
            # visitedChars is a dictionary which will store for every new iteration
            # characters that are unique and their indices starting from ith index
            visitedChars = {}
            localLen = 0
            # While s[i] is unique starting from ith index, we add that s[i], i key-val
            # pair to visitedChars and increase localLen by 1 and i by 1
            while i < len(s) and s[i] not in visitedChars:
                visitedChars[s[i]] = i
                localLen += 1
                i += 1
            # If the above is terminated because we found a duplicate char, then
            # i will be < len(s)
            if i < len(s):
                # Updating i to visitedChars[s[i]] + 1, since s[i] is already 
                # encountered before, and its index is visitedChars[s[i]].
                # That means starting from visitedChars[s[i]] to i there are only
                # unique chars
                i = visitedChars[s[i]] + 1
            globalLen = max(globalLen, localLen)
        
        return globalLen

######################################################

#   Optimal Solution

#   Runtime: 56ms   -   82.91%
#   Memory: 14.3MB  -   80.87%

######################################################

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        globalLen = 0
        # This appraoch is a sliding window approach and startIndex will be the
        # start index of the sliding window. End index will be i and it will constantly
        # move to right by 1
        startIndex = 0
        visitedChars = {}
        
        for i in range(len(s)):
            # If s[i] is already present in visitedChars, we move the startIndex of
            # sliding window to visitedChars[s[i]] + 1, if startIndex < 
            # visitedChars[s[i]] + 1. Why only if startIndex < visitedChars[s[i]] + 1
            # is, lets sat startIndex is currently at 3, and we have encountered a
            # char which is already present at 0. If we don't do this if check,
            # sliding window will again move to 0 and between the current sliding 
            # window, there will be another duplicate which will be avoided in further
            # iterations
            if s[i] in visitedChars:
                startIndex = max(startIndex, visitedChars[s[i]] + 1)
            # i - startIndex + 1 will give the current sliding window length.
            globalLen = max(globalLen, i - startIndex + 1)
            # Adding or updating the s[i] key in visitedChars dictionary
            visitedChars[s[i]] = i
        
        return globalLen