######################################################

#   Solved on Friday, 21 - 01 - 2022.

######################################################


######################################################

#   Linear Search Approach

#   Runtime: 122ms   -   43.82%
#   Memory: 14.2MB  -   99.78%

######################################################

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # Since, letters are in sorted order, if last letter is < target we can't
        # find the required letter. So, we return letters[0] as given in the question
        if ord(letters[-1]) <= ord(target): return letters[0]
        # Looping through letters
        for letter in letters:
            # If this condition is true, since letters is in sorted order letters to
            # left of this letter are <= target. So, this is our required letter
            # So we return it
            if ord(letter) > ord(target): return letter


######################################################

#   Binary Search Approach

#   Runtime: 130ms   -   40.83%
#   Memory: 14.4MB  -   92.63%

######################################################

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # Since, letters are in sorted order, if last letter is < target we can't
        # find the required letter. So, we return letters[0] as given in the question
        if ord(letters[-1]) <= ord(target): return letters[0]

        low = 0
        high = len(letters) - 1
        
        while low < high:
            mid = (low + high) // 2
            # Why we are setting high = mid but not mid - 1 is, since we need the
            # first largest letter than target, letter at mid might also be the required
            # letter. So, we set high to mid and we have while condition has low < high
            # unlike low <= high which might lead to infinite loop in some cases
            if ord(letters[mid]) > ord(target): high = mid
            else: low = mid + 1
        # Loop breaks when low == high. So, returning letters[low] or letters[high]
        # is same
        return letters[high]

