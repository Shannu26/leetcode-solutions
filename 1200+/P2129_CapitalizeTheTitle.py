######################################################

#   Solved on Monday, 24 - 01 - 2022.

######################################################


######################################################

#   Runtime: 32ms   -   87.38%
#   Memory: 13.9MB  -   98.61%

######################################################

class Solution:
    def capitalizeTitle(self, title: str) -> str:
        # Splitting the title using space
        words = title.split()
        
        title = ""
        # Looping through words
        for i in range(len(words)):
            # If word has < 3 chars it should have all lower case letter
            if len(words[i]) < 3: title += words[i].lower()
            # Else, first letter in word should be capitalized
            else: title += words[i].capitalize()
            # For last word, no need of trailing space right, So we are adding space
            # only if i < len(words) - 1
            if i != len(words) - 1: title += " "
        
        return title