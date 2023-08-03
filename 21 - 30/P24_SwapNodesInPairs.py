######################################################

#   Solved on Tuesday, 14 - 12 - 2021.

######################################################


######################################################

#   Runtime: 24ms   -   96.14%
#   Memory: 14.1MB  -   92.58%

######################################################

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Dummy node which points to head of given linked list. Why we need this node
        # is, once we swap 1st and 2nd nodes, 2nd node will be the first node in the
        # linked list. If we don't have a dummy node, we would have to use a separate
        # if statement to figure out that this is the 2nd node and assign head to it
        # Having a dummy node like this just smoothens the whole process logic.
        front = ListNode(0, head)
        # Movig head to front
        head = front
        
        while head != None and head.next != None and head.next.next != None:
            # Consider, 1 -> 2 -> 3 -> 4. After assigning Dummy node it becomes
            # 0 -> 1 -> 2 -> 3 -> 4. Let's say head is at 0. In our example
            # since we are at starting of linked list, for this iteration 
            # head and front both point to 0

            # temp will point to node 2. We need this because, once we point
            # 1 to 3, we will lose the reference to node 2. So we are storing
            # that node in temp
            temp = head.next.next
            # Pointing 1's next to 2's next which is 3. So, now
            # front = 0 -> 1 -> 3 -> 4 and temp = 2 -> 3 -> 4
            head.next.next = head.next.next.next
            # Pointing 2's next to head.next which is node 1. Now,
            # front = 0 -> 1 -> 3 -> 4 and temp = 2 -> 1 -> 3 -> 4
            temp.next = head.next
            # Pointing head's next to temp, i.e; 0's next to 2. Now,
            # front = 0 -> 2 -> 1 -> 3 -> 4 and temp = 2 -> 1 -> 3 -> 4
            head.next = temp
            # Moving head from 0 to next required node, which will be the previous
            # node of 3, since we swapped 1,2 and next we need to swap 3, 4. Now,
            # front = 0 -> 2 -> head and head = 1 -> 3 -> 4
            head = head.next.next
        
        # Since front points is a dummy node pointing to head which is the required
        # linked list, we return front.next
        return front.next