######################################################

#   Solved on Sunday, 31 - 10 - 2021.

######################################################


######################################################

#   Runtime: 28ms   -   92.94%
#   Memory: 14.2MB  -   60.90%

######################################################

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        strings = []
        def traverse(root, string):
            if root == None: return
            # If root.left and root.right are None, then root is a leaf node, so
            # we append string before encountering root and root.val to the 
            # strings list
            if root.left == None and root.right == None:
                strings.append(string + str(root.val))
                return 
            # Traversing left node and right node
            traverse(root.left, string + str(root.val) + "->")
            traverse(root.right, string + str(root.val) + "->")
        
        traverse(root, "")
        return strings