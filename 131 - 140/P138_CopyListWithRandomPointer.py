######################################################

#   Solved on Wednesday, 11 - 29 - 2023.

######################################################


######################################################

#   Runtime: 38ms   -   85.68%
#   Memory: 17.16MB  -   80.14%

######################################################

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # To Map memory address of nodes in original list
        # to an Index
        addrToIndex = {}
        # List to store created copy nodes. Initialized with
        # dummy node at first.
        nodeList = [Node(0, None, None)]
        pointer = head
        # Index is 1 since at index 0 I added dummy node
        index = 1

        # Looping through original Node
        while head:
            # Creating new copy node
            node = Node(head.val, None, None)
            # Updating next prop of previous node to 
            # this node
            nodeList[-1].next = node
            # Adding node to list
            nodeList.append(node)
            # Mapping address of current original node
            # to index
            addrToIndex[id(head)] = index
            index += 1
            head = head.next
        
        # To keep track of current node index
        nodeIndex = 1
        while pointer:
            # If node.random is pointing to some other
            # node
            if pointer.random:
                # Getting address of that node
                addr = id(pointer.random)
                # Getting Index of that node address in
                # list
                randomIndex = addrToIndex[addr]
                # Updating random pointer
                nodeList[nodeIndex].random = nodeList[randomIndex]
            pointer = pointer.next
            nodeIndex += 1
        # Since node at index 0 is dummy, returning
        # nodeList[0].next. Why not nodeList[1] is, if
        # given list is empty, there won't be any value
        # in nodeList[1]
        return nodeList[0].next
