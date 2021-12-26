######################################################

#   Solved on Friday, 03 - 09 - 2021.

######################################################


######################################################

#   Runtime: 32ms   -   80.74%
#   Memory: 14.1MB  -   99.28%

######################################################

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if len(strs) == 1: return strs[0]
        string = ""
        # index will be the current index position which char we are checking 
        # against all strings
        index = 0
        ended = False
        while not ended:
            for i in range(len(strs) - 1):
                # If current string or next string has a length == index, then there
                # won't be a char at index. So the process is ended.
                if index == len(strs[i]) or index == len(strs[i + 1]): 
                    ended = True
                    break
                # If char at index of string i and i+1 don't match then, we end the
                # process
                if strs[i][index] != strs[i + 1][index]:
                    ended = True
                    break
            # If process not ended, we add the current index char to the result string
            if not ended: 
                string += strs[0][index]
                index += 1
        
        return string