######################################################

#   Solved on Thursday, 10 - 26 - 2023.

######################################################


######################################################

#   O(26 * n) Approach

#   Runtime: 152ms   -   17.20%
#   Memory: 16.22MB  -   82.92%

######################################################

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
            The logic is to use sliding window approach to solve this
            problem.
            We continuously increase right pointer and store count of 
            characters in string for each value at right pointer.
            window length = right - left + 1
            We can say a window is valid if we can alter atmost k chars to
            get all same characters. So, it's best to alter all characters
            other than character with most frequency in that window.
            We find highest frequency and while window length is not valid
            we move left pointer.
            Window is not valid if 
                windowLen - maxFrequency > k
                which means we have more disimilar characters in our window
                than we can alter
            We update longestLen based on window length every time.
        """
        longestLength = 0
        charCounts = [0] * 26
        left = 0
        right = 0

        while right < len(s):
            charCounts[ord(s[right]) - 65] += 1
            # While window is not valid
            while right - left + 1 - max(charCounts) > k: 
                charCounts[ord(s[left]) - 65] -= 1
                left += 1
            
            longestLength = max(longestLength, right - left + 1)
            right += 1

        return longestLength

######################################################

#   O(n) Approach

#   Runtime: 89ms   -   79.58%
#   Memory: 16.22MB  -   82.92%

######################################################

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
            The logic is similar to above logic but with some optimality.
            Let's say we have a window length which is valid. If moving
            right pointer made it invalid, we can say that we have atleast
            previous window length which is valid right. So, instead of
            moving left pointer as long as window is not valid, we can just
            leave the window length  like that by moving left pointer only
            once right. If we find a right character which makes window
            valid, we will have new window with larger size. But, we can
            say for sure before that right character, this previous window
            length is the largest right.
            Also, to keep track of max frequency, instead of looping 
            everytime, we can update it if frequency of current right 
            character is greater right.Let's say when window became invalid
            left character has the highest frequency. So, when we move
            left pointer, highest frequency might change if another character
            has the same frequency of this character. But, it doesn't
            change the overall longest length right. So, we can just
            leave max frequency to that previous value and update it 
            when we find a character with greater frequency.
        """
        longestLength = 0
        charCounts = [0] * 26
        left = 0
        right = 0
        maxCount = 0

        while right < len(s):
            charCounts[ord(s[right]) - 65] += 1
            # Updating max frequency
            maxCount = max(maxCount, charCounts[ord(s[right]) - 65])
            # If window is invalid, moving left pointer by 1.
            if right - left + 1 - maxCount > k: 
                charCounts[ord(s[left]) - 65] -= 1
                left += 1
            
            longestLength = max(longestLength, right - left + 1)
            right += 1

        return longestLength
