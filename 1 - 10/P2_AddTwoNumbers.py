######################################################

#   Solved on Sunday, 03 - 07 - 2021.

######################################################


######################################################

#   Runtime: 56ms   -   99.13%
#   Memory: 14.1MB  -   97.54%

######################################################


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        # Pointer to head of resultant linked list
        front = l1
        # Carry variable to store the carry of previous sum, which at first is 0
        carry = 0
        
        # A pointer which points to prev node of current l1 node
        prev = l1
        while l1 != None and l2 != None:
            
            l1.val = l1.val + l2.val + carry
            
            # Logic to find carry is divisor of l1.val divided by 10
            carry = l1.val // 10
            # Logic to find l1.val is remainder of l1.val divided by 10
            l1.val = l1.val % 10
            
            prev = l1
            l1 = l1.next
            l2 = l2.next
        
        # Case - 1, where length of l2 number > l1 number
        while l2 != None:
            # We append a new node to prev node of resultant linked list which always
            # will be the end node of front, since in this case l1 has become None
            prev.next = ListNode(l2.val + carry)
            prev = prev.next
            l2 = l2.next

            carry = prev.val // 10
            prev.val = prev.val % 10
        
        # Case - 2, where length of l1 number > l2 number
        while l1 != None:
            l1.val = l1.val + carry
            carry = l1.val // 10
            l1.val = l1.val % 10
            
            # Updating prev pointer to current prev node
            prev = l1
            l1 = l1.next
        
        # If there is a carry then we need to append a new node with val as 1 to the
        # end of the linked list.
        if carry:
            # Since prev points to end node of current linked list, we append new node
            # to that node's next pointer
            prev.next = ListNode(1)
        
        return front        