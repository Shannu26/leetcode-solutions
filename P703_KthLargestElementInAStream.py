######################################################

#   Solved on Friday, 08 - 04 - 2022.

######################################################


######################################################

#   Runtime: 101ms   -   85.05%
#   Memory: 18MB  -   87.71%

######################################################

import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        # Converting self.heap into a Min-Heap. So, now if we remove an element
        # we get the min element every time.
        heapq.heapify(self.heap)
        # While there are > k elements in heap, we remove the min element. After
        # this loop ends we will have k elements if previously it has > k elements
        # Since it is a min-heap, next time if we pop we get the min element right.
        # Since there are k elements only, the min element we get is the kth largest
        # if we think in reverse order
        while len(self.heap) > k:
            heapq.heappop(self.heap)
        
    def add(self, val: int) -> int:
        # Adding val to heap.
        heapq.heappush(self.heap, val)
        # We have 2 cases,
        # a) During initialistion of this class, they passed only k-1 elements. In this
        # case kth largest will be the min-element in the heap
        # b) During initialistion of this class, they passed >= k elements. In this
        # case heap will have k elements before this call. After adding this new val
        # heap now has k+1 elements. So we have to remove min-element to again get
        # k elements in heap

        # b) case
        if len(self.heap) > self.k: heapq.heappop(self.heap)
        # Getting kth largest
        kthLargest = heapq.heappop(self.heap)
        # Again adding that popped element to heap
        heapq.heappush(self.heap, kthLargest)
        # Returning that kth largest
        return kthLargest
        
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)