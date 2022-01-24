######################################################

#   Solved on Monday, 24 - 01 - 2022.

######################################################


######################################################

#   Runtime: 28ms   -   91.10%
#   Memory: 14MB  -   91.67%

######################################################

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        # Word of length 1 will be always be valid. So we return True
        if len(word) == 1: return True
        # If last char in word is capital then all chars in the word should we
        # capital. So we are determining whether word should be all caps
        isCaps = 65 <= ord(word[-1]) <= 90
        # Looping through word from end to start
        for i in range(-2, -len(word) - 1, -1):
            # If word should have all caps according to isCaps but char at i has
            # small letter it is not a valid word. So we return False
            if 97 <= ord(word[i]) <= 122 and isCaps: return False
            # If isCaps is not true, word shouldn't have caps except for 1st char
            # which may or mayn't have caps. So we are checking if char at i is capital
            # If yes, last letter in word is small, but word at i is capital. So we
            # return False. We skip checking for 1st char because first char may or
            # maynot be capital even if all other chars should be small.
            if i != -len(word) and 65 <= ord(word[i]) <= 90 and not isCaps: return False
        # We reach here only if for loop ends. For loop ends normally if all chars
        # satisfy the constraints. So word is valid. So return True
        return True