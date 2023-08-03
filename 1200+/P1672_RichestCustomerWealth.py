######################################################

#   Solved on Tuesday, 01 - 02 - 2022.

######################################################


######################################################

#   Runtime: 52ms   -   86.21%
#   Memory: 13.9MB  -   99.25%

######################################################

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        
        maxWealth = -1
        
        for account in accounts:
            totalMoney = 0
            for money in account: totalMoney += money
            maxWealth = max(maxWealth, totalMoney)
        
        return maxWealth