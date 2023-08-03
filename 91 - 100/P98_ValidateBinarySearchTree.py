######################################################

#   Solved on Thursday, 05 - 08 - 2021.

######################################################


######################################################

#   Runtime: 44ms   -   71.47%
#   Memory: 16.2MB  -   94.65%

######################################################

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return Solution.isValid(root)
    
    def isValid(root, low = -math.inf, high = math.inf):
        
        if not root: return True
        
        if root.val <= low or root.val >= high: return False
        
        return (
                Solution.isValid(root.left, low, root.val) and 
                Solution.isValid(root.right, root.val, high)
            )