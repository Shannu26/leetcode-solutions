######################################################

#   Solved on Monday, 03 - 01 - 2022.

######################################################


######################################################

#   Runtime: 48ms   -   97.49%
#   Memory: 14.6MB  -   10.53%

######################################################

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
            We can use dynamic programming for this problem. Because, if we observe 
            combination of a target k can be obtained by using the combinations of
            target 0 to k - 1. Because, lets say we know combinations for target = 1, 
            2, 3, 4, 5. candidates = [2, 4] and target = 6.
            combinations of 6 == combinations of 4 + [2] and combinations of 2 + [4]
            since combinations of 4 have combinations to get target 4 and adding 2
            to it will give us the required target i.e; 6.
        """
        # dp array
        combinationSums = []
        # Finding combinations for 1 to target + 1 values
        for i in range(1, target + 1):
            # Stores the combinations of i value
            nextCombination = []
            # Looping through candiates
            for candidate in candidates:
                # If i < candidate, the subproblem i - candidate will be < 0. So, we
                # skip it
                if i < candidate: continue
                # If i == candidate, then [candidate] alone is the combination 
                # possible, so we append [candidate]
                if i == candidate: nextCombination.append([candidate])
                elif i > candidate:
                    # Looping through combinations of subproblem i - candidate. Since
                    # list is 0 indexed we subtract 1 from i - candidate to make it 0
                    # indexed
                    for combination in combinationSums[i - candidate - 1]:
                        # This condition is crucial. Because, if we don't have this
                        # we will get duplicate combinations of different permutation
                        # Example: [2,2,3] is a combination for 7. If we don't check
                        # whether candidate >= combination[-1] different permutaions
                        # will also get appended and we will get [2,2,3] [3,2,2]
                        # [2,3,2]
                        if combination[-1] <= candidate:
                            nextCombination.append(combination + [candidate])
            # Adding combinations of ith value to dp array
            combinationSums.append(nextCombination[:])
        # dp[-1] will have combinations of target. So we return it
        return combinationSums[-1]
        