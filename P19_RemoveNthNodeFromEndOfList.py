######################################################

#   Solved on Monday, 09 - 08 - 2021.

######################################################


######################################################

#   Approach 1 : Using Recursion

#   Runtime: 32ms   -   75.68%
#   Memory: 14.1MB  -   76.91%

######################################################

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Upon successful completion of remove() function the returned value will be
        # num of nodes in given list.
        num = Solution.remove(head, n)
        # We check if len of list == n, then that means we have to remove the fist node
        # So we do, head = head.next
        if num == n:
            head = head.next
        
        return head
    
    def remove(head, n):
        """
            It is recursive function which return 0 if head param is None, otherwise
            it recursively calls itself with params head.next and n.
            When recursive call is returned, the returned value will be equal to
            how many nodes there are present after the current node. So we check if
            number of nodes present after current node is equal to n. If yes, we have
            reached (n + 1)th node from end. So we do head.next = head.next.next
            Finally we return num + 1 to increase len of nodes from end by 1
        """
        if head == None: return 0
        
        num = Solution.remove(head.next, n)
        if num == n:
            head.next = head.next.next
        return num + 1

######################################################

#   Approach 2 : Without Recursion

#   Runtime: 28ms   -   92.08%
#   Memory: 14.1MB  -   76.91%

######################################################

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        numOfNodes = 0
        # Temporary pointer to first node of list
        front = head
        # Loop to find number of nodes in list
        while head != None:
            numOfNodes += 1
            head = head.next
        # We check if len of list == n, then that means we have to remove the fist node
        # So we do, head = head.next
        if numOfNodes == n:
            return front.next
        
        head = front
        # We have to be at (n+1)th position from end, to remove nth node from end.
        # So we loop from start till we reach that node
        while numOfNodes - n != 1:
            front = front.next
            numOfNodes -= 1
            
        front.next = front.next.next
        return head