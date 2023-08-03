######################################################

#   Solved on Tuesday, 18 - 01 - 2022.

######################################################


######################################################

#   Runtime: 240ms   -   95.94%
#   Memory: 15.3MB  -   95.75%

######################################################

class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        # Given, timSeries will have atleast 1 value. So, starting with duration in
        # totalDuration
        totalDuration = duration
        # We leave last element, since last element have no element to its right to cut
        # off the poison duration of last element. So, last element will definitely
        # run for duration seconds
        for i in range(len(timeSeries) - 1):
            # If the poison given at timeSeries[i]th second will have effect >=
            # start time of (i+1)th index, then (i+1)th poison will cut off the 
            # poison at ith index. So, the duration at this case will be
            # start time of (i+1) - start time of (i) which is
            # timeSeries[i + 1] - timeSeries[i]
            if timeSeries[i] + duration - 1 >= timeSeries[i + 1]:
                totalDuration += timeSeries[i + 1] - timeSeries[i]
            # If (i+1)th index won't cut off ith index poison duration, ith index
            # poison will run for duration seconds. So we add it
            else: totalDuration += duration
        
        return totalDuration