######################################################

#   Solved on Saturday, 24 - 07 - 2021.

######################################################


######################################################

#   Brute Force Approach  -  O(n^2)

#   Time Limit Exceeded
#   49 / 60 passed

######################################################

class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
            The brute force logic is to find the area for every pair of indices
            and find max of those and return it
        """
        maxArea = 0
        
        for i in range(len(height)):
            for j in range(i + 1, len(height)):
                maxArea = max(maxArea, (j - i) * min(height[j], height[i]))
        
        return maxArea

######################################################

#   Two pointer Approach  -  O(n)

#   Runtime: 656ms   -   94.51%
#   Memory: 27.3MB  -   83.81%

######################################################

class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        maxArea = 0

        # Initalising pointers at both ends of array
        first = 0
        last = len(height) - 1
        
        while first < last:
            # Since area between 2 heights depends on min of those 2 heights we first find
            # which is min and then find area with that height and width as 
            # last - first
            if height[first] < height[last] : 
                maxArea = max(maxArea, height[first] * (last - first))
                # Since we need maxArea and height[first] < height[last], always area
                # with an edge as height[last] will be > area with an edge as 
                # height[first]. so increment first by 1 to go to next index
                first += 1
            else: 
                maxArea = max(maxArea, height[last] * (last - first))
                # Since we need maxArea and height[first] > height[last], always area
                # with an edge as height[last] will be < area with an edge as 
                # height[first]. so decrement last by 1 to go to next index
                last -= 1
                
        return maxArea