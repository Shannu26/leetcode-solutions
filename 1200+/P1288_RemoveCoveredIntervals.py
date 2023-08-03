######################################################

#   Solved on Wednesday, 19 - 01 - 2022.

######################################################


######################################################

#   Runtime: 92ms   -   87.76%
#   Memory: 14.5MB  -   99.13%

######################################################

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        # Sorting the intervals
        intervals.sort()
        # variable to store the length of final intervals
        count = 0
        # index which points to last interval which is not covered by other intervals
        index = -1
        
        for i in range(len(intervals)):
            # Since, first interval has no left intervals, it can't be covered by other
            # So we set index to 0
            if i == 0: index = 0
            else:
                # Here 2 cases are possible.
                # a) both intervals at index and i have same start point and end point
                # of interval i is > end point of interval index. In this case, index
                # interval is covered by i interval. So, we change end point of index
                # interval to end point of i interval
                if intervals[index][0] == intervals[i][0] and intervals[index][1] < intervals[i][1]:
                    intervals[index][1] = intervals[i][1]
                # b) interval at i has both start and end point <= end point of interval
                # at index. In this case i interval is covered by index interval
                # If this condition fails, then interval i is not covered by index
                # So, it is a separate interval. It will increase the size of resultant
                # intervals array. So we increase count by 1. And we change index to i
                # because, now i interval is not covered by its previous intervals
                # So from next interations we need to compare with this interval, since
                # intervals are in sorted order
                elif not(intervals[index][1] >= intervals[i][0] and intervals[index][1] >= intervals[i][1]): 
                    index = i
                    count += 1
        # Since, we initialized count with 0 and at i = 0, we haven't incremented it
        # we need to add 1 to count
        return count + 1