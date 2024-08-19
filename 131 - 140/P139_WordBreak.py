######################################################

#   Solved on Thursday, 03 - 08 - 2022.

######################################################


######################################################

#   Runtime: 40ms   -   96.36%
#   Memory: 16.36MB  -   83.50%

######################################################

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        wordDict = set(wordDict)
        # dp array is a boolean array which tells us at each index i, whether
        # it is possible to break substring s[:i] into segments that are
        # part of wordDict 
        dp = [False] * (len(s) + 1)
        # Since dp[0] means substring s[:0] which is an empty string, it is 
        # possible to break it. So we set true
        dp[0] = True
        # Looping through the string length
        for i in range(1, len(s) + 1):
            # Looping through substring s[:i]
            for j in range(i):
                # At each step we check whether s[0:j] can be split into
                # segments that are part of wordDict which is stored in dp[j]
                # If yes, we check if substring s[j:i] in wordDict.
                # If yes, then we can split s[:i] into 2 parts s[0:j] and 
                # s[j:i] where s[0:j] can be further splitted into parts 
                # which are part of wordDict
                if dp[j] and s[j:i] in wordDict:
                    # So, we set dp[i] to True and break the loop
                    dp[i] = True
                    break
        # We return value in dp[-1] which has solution for whether we can
        return dp[-1]