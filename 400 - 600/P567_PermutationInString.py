######################################################

#   Solved on Friday, 11 - 03 - 2023.

######################################################


######################################################

#   O(26 * N) Approach

#   Runtime: 53ms   -   96.99%
#   Memory: 16.22MB  -   88.83%

######################################################

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
            The logic is to use a sliding window of length s1.
            We use 2 arrays of size 26 to count the characters present
            in that window size, one to count characters in s1, one for 
            sliding window size of s2.
            For every sliding window, we check if count of s1 == s2 which
            takes O(26) time.
            After that we move sliding window to the right by updating count
            array of s2.
            We return true if s1 == s2 for any sliding window.
        """
        if len(s2) < len(s1): return False

        s1Count = [0] * 26
        s2Count = [0] * 26

        for index in range(len(s1)):
            # Counting for first sliding window
            s1Count[ord(s1[index]) - 97] += 1
            s2Count[ord(s2[index]) - 97] += 1

        left = 0
        for right in range(len(s1), len(s2)):
            if s1Count == s2Count: return True
            # Moving sliding window to right by removing left character from
            # count and adding right character to count
            s2Count[ord(s2[left]) - 97] -= 1
            left += 1
            s2Count[ord(s2[right]) - 97] += 1
        
        return s1Count == s2Count

######################################################

#   O(N) Approach

#   Runtime: 51ms   -   98.23%
#   Memory: 16.22MB  -   88.83%

######################################################


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
            This is an optimization of above approach. Instead of
            checking all 26 counts everytime to see if they are equal,
            since we are updating counts of left and right characters of
            window, we can just compare them to check whether that window
            is same of s1.
            We will have a matches variable which keeps track of number of
            matches between s1 and s2 for each sliding window. If matches == 26
            then both are equal.
        """

        if len(s2) < len(s1): return False

        s1Count = [0] * 26
        s2Count = [0] * 26

        for index in range(len(s1)):
            s1Count[ord(s1[index]) - 97] += 1
            s2Count[ord(s2[index]) - 97] += 1

        matches = 0
        for i in range(26):
            # Finding matches for first window
            if s1Count[i] == s2Count[i]: matches += 1

        left = 0
        for right in range(len(s1), len(s2)):
            if matches == 26: return True

            # Updating left character count
            index = ord(s2[left]) - 97
            s2Count[index] -= 1
            # If equal, that means previously they were unequal. So we got a new
            # match. Update the matches
            if s2Count[index] == s1Count[index]: matches += 1
            # If unequal, there might be a chance that they were unequal before this
            # as well right. We can say if we got a mismatch from a match previously
            # when previously it was a match. Since we are reducing count by 1, we
            # check if adding 1 to current count makes it same as s1Count. If yes, we
            # got a new mismatch. Reduce matches by 1
            elif s2Count[index] + 1 ==  s1Count[index]: matches -= 1

            index = ord(s2[right]) - 97
            s2Count[index] += 1
            # If equal, that means previously they were unequal. So we got a new
            # match. Update the matches
            if s2Count[index] == s1Count[index]: matches += 1
            # If unequal, there might be a chance that they were unequal before this
            # as well right. We can say if we got a mismatch from a match previously
            # when previously it was a match. Since we are incrementing count by 1, we
            # check if subtracting 1 to current count makes it same as s1Count. If yes, we
            # got a new mismatch. Reduce matches by 1
            elif s2Count[index] - 1 == s1Count[index]: matches -= 1

            left += 1

        return matches == 26