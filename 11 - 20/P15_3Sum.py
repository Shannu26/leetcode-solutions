######################################################

#   Solved on Wednesday, 25 - 08 - 2021.

######################################################


######################################################

#   Runtime: 792ms   -   80.44%
#   Memory: 17.4MB  -   86.77%

######################################################

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
            The logic is simple. We sort the array and we perform logic similar
            to twoSum on nums[i + 1] to end of list for every nums[i].
            To avoid duplicates, we skip loops where nums[i] == nums[i-1], Since
            they both generate the same outcome. For target value, since we need 
            to get 0 and we already have nums[i], we still need 0 - nums[i]. So
            we send -1 * nums[i] as target
        """
        result = []
        nums.sort()
        
        for i in range(len(nums)):
            if i != 0 and nums[i] == nums[i - 1]: continue
            Solution.twoSum(nums, -1 * nums[i], result, i + 1)
            
        return result
    
    def twoSum(nums, target, result, startIndex):
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
            # visited. If not we add [nums[startIndex - 1], nums[dictionary[nums[i]]], nums[i]]
            # to result array and (nums[dictionary[nums[i]]], nums[i]) to visited set
            if nums[i] in dictionary:
                if (nums[dictionary[nums[i]]], nums[i]) not in visited:
                    result.append([nums[startIndex - 1], nums[dictionary[nums[i]]], nums[i]])
                    visited.add((nums[dictionary[nums[i]]], nums[i]))
            # If nums[i] is not already present, then we add its complementary val i.e;
            # target - nums[i] into dictionary as key and i as val
            else:
                dictionary[target - nums[i]] = i