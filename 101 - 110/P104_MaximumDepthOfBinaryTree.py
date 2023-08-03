######################################################

#   Solved on Friday, 21 - 01 - 2022.

######################################################


######################################################

#   Runtime: 32ms   -   98.64%
#   Memory: 15.9MB  -   71.28%

######################################################

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # If root != None, max depth of root will be max depth of its subtrees + 1
        if root: return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
        # If root == None, that means there are no nodes. So no possibility of depth
        # So, we return 0
        return 0