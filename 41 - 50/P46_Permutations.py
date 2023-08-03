######################################################

#   Solved on Tuesday, 02 - 11 - 2021.

######################################################


######################################################

#   Runtime: 32ms   -   97.78%
#   Memory: 14.4MB  -   71.09%

######################################################

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        permutations = []
        def solve(permutation):
            if len(permutation) == len(nums):
                # If len of permutation becomes len of nums array, that means we
                # reached the next permutation. So we append it to the result list
                permutations.append(permutation)
                return
            
            for num in nums:
                if num not in permutation:
                    # If number is not yet present in the permuation list, we
                    # add it to the list and recursively call solve function
                    solve(permutation + [num])
            
        solve([])
        return permutations