######################################################

#   Solved on Tuesday, 07 - 04 - 2021.

######################################################

######################################################

#   Runtime: 56ms   -   97.72%
#   Memory: 14.7MB  -   99.38%

######################################################


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
    	"""
    		We can solve this problem optimally in O(n) using Kadane's Algorithm
    		which follows Dynamic Programming Strategy.

    		If we observe clearly considering indices fron end to start, we will know
    		that max_subarray_sum of a subarray having index i is either nums[i] or
    		nums[i] + max_subarray_sum[i - 1]. Why it works is, consider [-1, 2, 1].
    		at i = 1, we can clearly see that max_subarray is just [2], since [-1,2]
    		gives sum less than the current index value. When nums[i] > (nums[i] + 
    		max_subarray_sum[i - 1]) it is worthless to still consider the previous 
    		subarray since subarray starting from nums[i] will always give more sum
    		than subarray considering indices previous to that i.

    		We can optimize the memory, by not taking an array to store the max 
    		subarray sum of previous indices, but just take a variable to store
    		max subarray sum of i - 1 index. since after all we just need that value
    		to find current subarray sum
    	"""
        
        # Initalizing current max and global max to nums[0] since here i = 0
        local_max_at_index_i = nums[0]
        global_max = nums[0]
        
        for i in range(1, len(nums)):
            local_max_at_index_i = max(local_max_at_index_i + nums[i], nums[i])
            global_max = max(global_max, local_max_at_index_i)
        
        return global_max