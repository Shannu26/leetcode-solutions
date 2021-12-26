######################################################

#   Solved on Monday, 11 - 10 - 2021.

######################################################


######################################################

#   Runtime: 916ms   -   85.53%
#   Memory: 14.2MB  -   93.33%

######################################################

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1: return s
        # Pointers to the starting and ending index of longest palindrome
        start = end = 0
        # The logic is, we loop through each index of the string and at each index
        # there are 2 possibilities of palindrome having s[i] at the center of
        # that palindrome.
        # They are palindrome of odd length having s[i] at the middle of that string
        # and even length having s[i] at left of the middle of that string
        # We will find possible longest palindrome lengths for that 2 cases and 
        # consider the max of those 2 as the longest palindrome substring having s[i]
        # at its center
        for i in range(len(s)):
            len1 = Solution.expandFromCenter(s, i, i)
            len2 = Solution.expandFromCenter(s, i, i + 1)
            length = max(len1, len2)
            # If curr length is better than already existing length of longest 
            # palindrome, we update those pointers by moving half length away from i
            # to the left for start pointer and to the right for end pointer
            if length > end - start:
                start = i - ((length - 1) // 2)
                end = i + (length // 2)
        # Return the substring
        return s[start:end + 1]
    
    def expandFromCenter(s, left, right):
        """
            This method helps in finding the longest palindrome length starting from
            left, right pointers and expanding both sides till we reach end of string
            or s[left] and s[right] are not equal
        """
        if s == "" or left > right: return 0
        
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # Why we return right - left - 1 is, the above loop breaks if we reach end of 
        # string or s[left] != s[right]. Since left, right positions are not to be 
        # included in the length. We will do right - left. Since string is 0 indexed
        # we change that into index by subtracting 1 from it. so right - left - 1
        return right - left - 1