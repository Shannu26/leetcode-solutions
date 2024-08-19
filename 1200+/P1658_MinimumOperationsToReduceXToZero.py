######################################################

#   Runtime: 924ms   -   93.72%
#   Memory: 30.22MB  -   82.51%

######################################################

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        """
            To solve the problem in optimal way, think of it in different
            angle. That is, instead of finding which elements to remove
            to get sum of x, find a contiguous subarray in the list which
            sum to (total sum of nums - x). If we find it, the remaining
            elements sum will definitely equal to x.
        """
        minOperations = -1
        total = sum(nums)
        # If total of nums < x, we can never find x. So return -1
        if total < x: return -1
        # If total == x, we need to remove all elements.
        if total == x: return len(nums)
        # total - x
        remainder = total - x
        # contiguous subaray sum
        subsum = 0
        # left pointer of subarray to find total length of subarray
        left = 0
        # right pointer looping
        for right in range(len(nums)):
            # updating subarray sum
            subsum += nums[right]
            # If subsum > total - x, we need to remove some elements from
            # subarray from left side
            while subsum > remainder:
                subsum -= nums[left]
                left += 1
            # If subsum == total - x, 
            #   length of subarray == right - left + 1
            #   So, number of elements we need to remove == 
            #           len(nums) - length of subarray
            # Since, we need minOperations, we are storing only min value
            # of that len(nums) - length of subarray
            if subsum == remainder:
                if minOperations == -1: minOperations = math.inf
                minOperations = min(minOperations, len(nums) - (right - left + 1))
        
        return minOperations   