######################################################

#   Solved on Tuesday, 18 - 01 - 2022.

######################################################


######################################################

#   Runtime: 64ms   -   99.87%
#   Memory: 17.4MB  -   92.84%

######################################################

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # If given intervals have no elements, we have to insert newInterval at the 
        # start only. So we return [newInterval]
        if len(intervals) == 0: return [newInterval]
        finalIntervals = []
        index = 0
        # Finding the index where the newInterval fits. Options are
        # a) start point of interval is in range [intervals[index][0], intervals[index][1]]
        # b) start point of interval is less than intervals[index[0]]
        # In these 2 cases, start point of new interval fits at index position
        # In those cases, we break out of loop
        # Else,we add current interval to finalIntervals and we increase index by 1
        for interval in intervals:
            if interval[0] <= newInterval[0] <= interval[1] or newInterval[0] < interval[0]: break
            index += 1
            finalIntervals.append(interval)
        else:
            # This else will execute only if for loop has executed completely without
            # breaking out of loop. It happens when we iterate all intervals and haven't
            # found the spot. This means that the new interval is > all intervals
            # So, we append it to end of finalIntervals and return 
            return finalIntervals + [newInterval]
        # In case (b), there is a probability that even end point of new interval is
        # less than start point of intervals[index]. In that case, there won't be any
        # merging of intervals if we insert new interval. So,we just have to insert 
        # the new interval 
        if newInterval[0] < intervals[index][0] and newInterval[1] < intervals[index][0]:
            finalIntervals.append(newInterval)
        # If that special case in (b) is not true, start point will be min of
        # start point of new interval or intervals[index]
        # End point as of now will be end point of intervals[index], since we haven't
        # checked for overlaps with next indices
        else:
            finalIntervals.append(intervals[index])
            finalIntervals[-1][0] = min(newInterval[0], intervals[index][0])
            # Now, we are finding the merges with next intervals. There will be merges
            # if end point of new interval >= start point of intervals[index]
            # So, we loop till that condition is true and increase index by 1
            while index < len(intervals) and newInterval[1] >= intervals[index][0]: index += 1
            # Now, we change the end point of last interval we inserted in finalIntervals
            # with actual value which is max(newInterval[1], intervals[index - 1][1])
            # Why index - 1 is, we come out of loop if condition fails. Condition failed
            # at index. So, index - 1 holds the required end interval value.
            finalIntervals[-1][1] = max(newInterval[1], intervals[index - 1][1])
        # After inserting the new interval and handling all the merges, we need to
        # add all the remaining intervals which don't merge with new interval. Here,
        # we are doing that
        while index < len(intervals):
            finalIntervals.append(intervals[index])
            index += 1
        
        return finalIntervals