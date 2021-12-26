######################################################

#   Solved on Tuesday, 30 - 11 - 2021.

######################################################


######################################################

#   Runtime: 28ms   -   98.39%
#   Memory: 14.2MB  -   86.69%

######################################################

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Dummy node to point to the sorted list
        head = ListNode()
        # Temporary pointer which moves to next empty slot where we should add next
        # node
        pointer = head
        # While either of lists are not empty
        while list1 != None and list2 != None:
            # If list1.val < list2.val, we add list1 node to pointer.next and
            # we move list1 to next node
            if list1.val < list2.val: 
                pointer.next = list1
                list1 = list1.next
            # If list2.val < list1.val, we add list2 node to pointer.next and
            # we move list2 to next node
            else:
                pointer.next = list2
                list2 = list2.next
            # Moving pointer to next node
            pointer = pointer.next
        
        # If there are still some nodes in list1, that means we break out of loop
        # because, list2 became empty, so we directly point pointer.next to list1
        # which is the first node of remaining elements of list1
        if list1 != None: pointer.next = list1
        # If there are still some nodes in list2, that means we break out of loop
        # because, list1 became empty, so we directly point pointer.next to list2
        # which is the first node of remaining elements of list2
        if list2 != None: pointer.next = list2
        
        # Since, head node is a dummy node which points to sorted list, we return
        # next node of head i.e; head.next  
        return head.next

