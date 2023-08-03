######################################################

#   Solved on Thursday, 07 - 04 - 2022.

######################################################


######################################################

#   Runtime: 33ms   -   82.82%
#   Memory: 13.9MB  -   68.03%

######################################################

import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # heapq is a Min-Heap implementation. Since we need max elements every time
        # I multiplied each element by -1
        stones = [-1 * stone for stone in stones]
        # Changed the stones array to a heap
        heapq.heapify(stones)
        # While we have >= 2 stones left
        while len(stones) > 1:
            # Getting top 2 elements and multiplying by -1 to get the original values
            firstStone = -1 * heapq.heappop(stones)
            secondStone = -1 * heapq.heappop(stones)
            # If both stones have same weight, both will get destroyed
            # Otherwise, smaller stone is destroyed and larger stone will have
            # weight large stone weight - small stone weight
            # Adding that weight to heap
            if firstStone != secondStone:
                heapq.heappush(stones, -1 * abs(firstStone - secondStone))
        # stones will be empty if last 2 stones we get have same weight
        # Otherwise we have 1 stone left
        return -1 * stones[0] if stones else 0