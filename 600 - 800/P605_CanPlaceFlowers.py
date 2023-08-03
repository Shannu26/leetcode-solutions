######################################################

#   Solved on Tuesday, 18 - 01 - 2022.

######################################################


######################################################

#   Runtime: 156ms   -   96.16%
#   Memory: 14.4MB  -   95.37%

######################################################

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        if n == 0: return True
        if len(flowerbed) == 1: return n == 1 and flowerbed[0] == 0
        
        for i in range(len(flowerbed)):
            # If flowerbedi] == 1, we can't plant new flower at i. so we skip the 
            # current iteration
            if flowerbed[i] == 1: continue
            # If i == 0, we need not check whether its previous index has 0 or 1.
            # So, we check if next index is not 1. If yes, we place 1 at i and decrease
            # n by 1
            if i == 0:
                if flowerbed[i + 1] != 1:
                    flowerbed[i] = 1
                    n -= 1
            # If i == len(flowerbed) - 1, we need not check whether its next index has
            # 0 or 1. So, we check if prev index is not 1. If yes, we place 1 at i 
            # and decrease n by 1
            elif i == len(flowerbed) - 1:
                if flowerbed[i - 1] != 1:
                    flowerbed[i] = 1
                    n -= 1
            # If i is neither 0 nor len(flowerbed) - 1, we check if both prev and next
            # indexes are not 1. If yes, we place 1 at i and decrease n by 1
            elif flowerbed[i - 1] != 1 and flowerbed[i + 1] != 1:
                flowerbed[i] = 1
                n -= 1
            # If n becomes 0, that means we have planted the required number of plants
            # So, we return True
            if n == 0: return True
        # We come out of for loop only if n != 0. So, we weren't able to place the
        # required number of flowers. So, return False
        return False