######################################################

#   Solved on Tuesday, 30 - 11 - 2021.

######################################################


######################################################

#   Runtime: 904ms   -   63.18%
#   Memory: 14.2MB  -   93.11%

######################################################

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        nums.sort()
        result = []
        
        # We perform logic similar to threeSum on nums[first + 1] to end of list for
        # every nums[first]. To avoid duplicates, we skip loops where nums[first] ==
        # nums[first - 1], since they both generate the same outcome. 
        for first in range(len(nums)):
            if first != 0 and nums[first] == nums[first - 1]: continue

            #### Three Sum Logic begins here.
            # We perform logic similar to twoSum on nums[second + 1] to end of list
            # for every nums[second]. To avoid duplicates, we skip loops where 
            # nums[second] == nums[second - 1], since they both generate the same
            # outcome. For target value, since we need to get "target" and we already 
            # have nums[first] + nums[second, we still need target - nums[first] - nums[second].
            # So we send target - nums[first] - nums[second] as target to twoSum 
            # function
            for second in range(first + 1, len(nums)):
                if second != first + 1 and nums[second] == nums[second - 1]: continue
                Solution.twoSum(nums, target - (nums[first] + nums[second]), result, first, second, second + 1)
                
        return result
                
    def twoSum(nums, target, result, firstIndex, secondIndex, startIndex):
        """
            We take a dictionary, which stores target - nums[i] as key and i as val.
            Visited set is used to check for duplicate pairs.
        """
        dictionary = {}
        visited = set()
        for i in range(startIndex, len(nums)):
            # If nums[i] is already in dictionary, that means we have already 
            # encountered the complementary val of nums[i] before ith index.
            # So we check whether (nums[dictionary[nums[i]]], nums[i]) is already
            # visited. If not we add [nums[firstIndex], nums[secondIndex], nums[dictionary[nums[i]]], nums[i]]
            # to result array and (nums[dictionary[nums[i]]], nums[i]) to visited set
            if nums[i] in dictionary:
                if (nums[dictionary[nums[i]]], nums[i]) not in visited:
                    result.append([nums[firstIndex], nums[secondIndex], nums[dictionary[nums[i]]], nums[i]])
                    visited.add((nums[dictionary[nums[i]]], nums[i]))
            # If nums[i] is not already present, then we add its complementary val i.e;
            # target - nums[i] into dictionary as key and i as val
            else:
                dictionary[target - nums[i]] = i