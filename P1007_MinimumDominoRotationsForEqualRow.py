######################################################

#   Solved on Tuesday, 25 - 01 - 2022.

######################################################


######################################################

#   Runtime: 1176ms   -   61.11%
#   Memory: 15MB  -   96.26%

######################################################

class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        # Stores the count of top and bottom values of first domino
        # Why only first domino's top and bottom is to make all dominoes
        # same number on either top or bottom, all other dominoes should match
        # either top or bottom of 1st domino
        # Structure is [
        #               count of tops[0] in top side of dominoes,
        #               count of tops[0] in bottom side of dominoes,
        #               count of tops[0] in both top and bottom sides
        #               ]
        # Why we need 3rd count too is, there are possibilites where both top and
        # bottom have same value. For that case no need of rotations right. For that
        # we use count of both top and bottom which will increase only by 1 even if
        # top and bottom of a domino are equal
        counts = {
            tops[0]: [0, 0, 0], 
        }
        # There are possibilities for bottoms[0] == tops[0]. In that case we only
        # need to use tops[0]
        if bottoms[0] not in counts: counts[bottoms[0]] = [0, 0, 0]
        # Looping through the dominoes
        for i in range(len(tops)):
            # If both tops[i] and bottoms[i] != either of tops[0] or bottoms[0]
            # solution is not possible. So we return -1
            if ( tops[i] not in counts and bottoms[i] not in counts ): return -1
            # If tops[i] is either tops[0] or bottoms[0], increasing top count and
            # total count
            if tops[i] in counts: 
                counts[tops[i]][0] += 1 
                counts[tops[i]][2] += 1
            # If bottoms[i] is either tops[0] or bottoms[0], increasing bottom count
            # and total count 
            if bottoms[i] in counts:
                counts[bottoms[i]][1] += 1 
                counts[bottoms[i]][2] += 1
            # If tops[i] and bottoms[i] are equal we need only +1 in total count
            # But in above 2 lines, it is increased by 2. So we reduce by 1
            if tops[i] in counts and tops[i] == bottoms[i]: counts[tops[i]][2] -= 1

        # If tops[0] total is len(tops) then, we can either rotate tops[0] present
        # in top to get same number in bottom or rotate tops[0] present in bottom
        # to get same number of top. But, we need min of these 2. So we return min 
        # of those 2
        if counts[tops[0]][2] == len(tops): 
            return min(counts[tops[0]][2] - counts[tops[0]][0], counts[tops[0]][2] - counts[tops[0]][1])
        # If bottoms[0] total is len(tops) then, we can either rotate bottoms[0] present
        # in top to get same number in bottom or rotate bottoms[0] present in bottom
        # to get same number of top. But, we need min of these 2. So we return min 
        # of those 2
        if counts[bottoms[0]][2] == len(tops):
            return min(counts[bottoms[0]][2] - counts[bottoms[0]][0], counts[bottoms[0]][2] - counts[bottoms[0]][1])
        # If total of both tops[0] and bottoms[0] are not equal to len(tops), we can't
        # make any side totally same. So we return -1
        return -1