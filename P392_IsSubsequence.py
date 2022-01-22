######################################################

#   Solved on Friday, 21 - 01 - 2022.

######################################################


######################################################

#   Runtime: 28ms   -   91.80%
#   Memory: 14.2MB  -   91.76%

######################################################

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # If s is empty string, we can make that string from t by removing all
        # chars. So, we return True
        if len(s) == 0: return True
        # If t is empty string, since we reach here only if s is not empty, we can't
        # a non empty string from empty string. So, we return False 
        if len(t) == 0: return False
        # index points to the index of current char in s which we are looking in t
        index = 0
        # Looping through the t string
        for i in range(len(t)):
            # If char at s[index] matches t[i], we can say that we can make substring
            # s[0] to s[index] using substring t[0] to t[i]. So, we need to check whether
            # chars of s from index + 1 to end can be made using string t from i + 1 to
            # end. So, we move index pointer to next index
            if s[index] == t[i]: index += 1
            # If s can be made from t[0] to t[i], after all index pointer movements
            # index will reach end of s i.e; index becomes len(s). If it happens
            # we can conclude that s is a subsequence of t. So we return True
            if index == len(s): return True
        # We will reach here, if for loop ends. For loops ends with function being
        # returned if we traversed entire t string, but we didn't reach end of s
        # i.e; index != len(s). Since, t have no chars left after end char we can't
        # make s[index] to s[-1] from empty string. So, we return False
        return False