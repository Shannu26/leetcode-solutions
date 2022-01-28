######################################################

#   Solved on Friday, 28 - 01 - 2022.

######################################################


######################################################

#   Runtime: 52ms   -   90.96%
#   Memory: 17.4MB  -   20.67%

######################################################

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        # If depth is 1, we have to add that val as root node. Its left child should
        # be the actual root node
        if depth == 1:
            # Creating new node with val and left child as root
            node = TreeNode(val, root, None)
            # Returning it
            return node
        # DFS Logic
        def traverse(root, d):
            # root node of subtree and d = depth of that root node
            # If root is None, we can't do anything. So return 
            if not root: return
            # We have to add that node at depth. So, node at depth - 1 should have
            # left and right childs as that node.
            # If current depth is depth - 1
            if d == depth - 1:
                # Creating left node with left child as root.left
                node1 = TreeNode(val, root.left, None)
                # Creating right node with right child as root.right
                node2 = TreeNode(val, None, root.right)
                # Pointing new left and right node to root.left and root.right
                root.left = node1
                root.right = node2
                # Process is over. So return 
                return
            # If d != depth - 1, we go to next depth
            traverse(root.left, d + 1)
            traverse(root.right, d + 1)
        # Starting the traversal with root and depth as 1
        traverse(root, 1)
        # We are performing the transformation on root node itself. So  we return it
        return root