######################################################

#   Solved on Thursday, 27 - 01 - 2022.

######################################################


######################################################

#   Runtime: 24ms   -   97.60%
#   Memory: 13.8MB  -   100.00%

######################################################

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        i = 0
        string = ""
        # Adding alternate chars to string while there are still chars left
        # in any one of the string
        while i < len(word1) and i < len(word2):
            string += word1[i] + word2[i]
            i += 1
        # If word1 has more chars than word2, adding them at the end
        while i < len(word1):
            string += word1[i]
            i += 1
        # If word2 has more chars than word1, adding them at the end
        while i < len(word2):
            string += word2[i]
            i += 1
            
        return string