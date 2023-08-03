######################################################

#   Solved on Saturday, 29 - 01 - 2022.

######################################################


######################################################

#   Runtime: 248ms   -   67.68%
#   Memory: 15.3MB  -   98.58%

######################################################

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        # counts is a dictionary having structure
        # number present in nums array as key
        # [count of that number, start index of that number] as value
        counts = {}
        # Stores the max degree
        degree = 0
        # Stores the required minSize
        minSize = math.inf
        # Looping through numbers
        for i in range(len(nums)):
            if nums[i] not in counts:
                # If nums[i] is not already present in counts
                # Iniitalize it with count 1 and start index as i
                counts[nums[i]] = [1, i] 
            else: 
                # If nums[i] is already present, increasing count of it by 1
                counts[nums[i]][0] += 1
            # If count of nums[i] > degree then we change value of degree
            # Since as of now nums[i] has max degree minSize list should include
            # all instance of nums[i]. That is start index of nums[i] till index i
            # start index is stored in counts[nums[i]][1]. So we change minSize
            # to i - counts[nums[i]][1] + 1 and degree to count of nums[i]
            if degree < counts[nums[i]][0]:
                degree = counts[nums[i]][0]
                minSize = i - counts[nums[i]][1] + 1
            # If degree not < count of nums[i] but == to it, that means 2 elements
            # have same degree. We can include any of them in our subarray. Since we
            # need min size of subarray there is a possibility that nums[i] elements
            # are closer than exisiting subarray
            # Ex: [1, 3, 2, 1, 2]. At last index we get to know that both 1 and 2 have
            # degree 2. Before last index there is only 1 having max count. So the 
            # minSize was 4. But if we consider subarray for 2 we can get it with
            # minSize of 3 only
            elif degree == counts[nums[i]][0]:
                # If subaaray length of start and end index of nums[i] < minSize
                # we change minSize to that length
                if i - counts[nums[i]][1] + 1 < minSize:
                    minSize = i - counts[nums[i]][1] + 1
        
        return minSize