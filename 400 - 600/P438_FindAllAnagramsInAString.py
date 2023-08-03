######################################################

#   Solved on Wednesday, 02 - 02 - 2022.

######################################################


######################################################

#   Runtime: 108ms   -   91.78%
#   Memory: 15.2MB  -   77.41%

######################################################

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # Counting the chars present in the p string
        pCounts = {}
        for char in p:
            if char not in pCounts:
                pCounts[char] = 1
            else:
                pCounts[char] += 1
        
        sCounts = {}
        anagramIndices = []
        # Represents the start index of substring which might be an anagram
        startIndex = 0
        
        for i in range(len(s)):
            # If char at s[i] is not in p, we can't make anagram using s[i]
            # as any position in the substring
            if s[i] not in pCounts:
                # So, I'm clearing the sCounts if they previous have some char counts
                sCounts = {}
                # Moving startIndex to i + 1 since we can't make any anagram using 
                # char at s[i]
                startIndex = i + 1
            else:
                # If s[i] is in pCounts and not in sCounts, initializing it with 1
                if s[i] not in sCounts: sCounts[s[i]] = 1
                # Else, incremeneting s[i] count by 1
                else: sCounts[s[i]] += 1
                # If substring from start index to i is of length len(p), this will
                # be an anagram if both pCounts and sCounts have same char counts
                if i - startIndex == len(p) - 1:
                    # We are checking that
                    for char in pCounts:
                        # If char is not in sCounts the chance is that both p and
                        # s[startIndex:i + 1] have same number of chars but in place
                        # of char, in s we have another char more number of times
                        # than required for us. So, we break loop since it is not
                        # an anagram
                        if char not in sCounts: break
                        # If char count in p and s[startIndex:i + 1] doesn't match
                        # it is not an anagram. so we break loop
                        if pCounts[char] != sCounts[char]: break
                    # This else will execute only if we exit the loop normally without
                    # any break statements. It will happen only if both are anagrams
                    # So, we append startIndex to result
                    else: anagramIndices.append(startIndex)
                    # Since we have used startIndex char and in next iteration we 
                    # move startIndex to next char we are reducing count of char at
                    # startIndex of s from sCounts by 1
                    sCounts[s[startIndex]] -= 1
                    # Moving startIndex to next point
                    startIndex += 1
        
        return anagramIndices