######################################################

#   Solved on Wednesday, 21 - 07 - 2021.

######################################################


######################################################

#   Runtime: 80ms   -   92.04%
#   Memory: 16.1MB  -   83.86%

######################################################

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        sol = []

        # Sorting the intervals based on starti i.e; intervals[i][0]
        intervals.sort()
        
        for interval in intervals:
            
            # Adding the first interval
            if len(sol) == 0: sol.append(interval)
            else:

                # If starting of current interval overlaps with last interval in the 
                # sol list, then we replace the end interval of sol[-1] i.e; sol[-1][1]
                # with max of current end interval and sol[-1][1]
                if interval[0] <= sol[-1][1]: sol[-1][1] = max(interval[1], sol[-1][1])
                # If no overlap, add the current interval to end of sol list
                else: sol.append(interval)
        
        return sol