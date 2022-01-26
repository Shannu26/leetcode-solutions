######################################################

#   Solved on Tuesday, 25 - 01 - 2022.

######################################################


######################################################

#   Runtime: 196ms   -   89.44%
#   Memory: 15.4MB  -   87.22%

######################################################


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        
        if len(arr) < 3: return False
        # If first element is the peak element, it is not a mountain since it has
        # no up slope. So, return Fasle
        if arr[0] > arr[1]: return False
        peakFound = False
        
        for i in range(len(arr) - 1):
            # Mountain should have strictly increasing or decreasing elements. So,
            # having equal elements means not a mountain
            if arr[i] == arr[i + 1]: return False
            # If we found a peak element, we set peakFound to True
            if arr[i] > arr[i + 1]: peakFound = True
            else:
                # If arr[i] < arr[i + 1] but, we have already found a peak element
                # before i, then it should not be possible to be a valid mountain
                # So, we return False, if peak was found and arr[i] < arr[i + 1]
                if peakFound: return False
        # peakFound will be False only if arr[i] > arr[i + 1] is not true for 
        # any index. It will have True, if we have a peak. We reach this line
        # only when above return False statements haven't executed. So mountain
        # is valid if peakFOund is True. So we return it
        return peakFound