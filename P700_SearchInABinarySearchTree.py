######################################################

#   Solved on Thursday, 14 - 04 - 2022.

######################################################


######################################################

#   Recursive Approach

#   Runtime: 78ms   -   86.45%
#   Memory: 16.4MB  -   96.41%

######################################################

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        if root:
            if val == root.val: return root
            if val < root.val: return self.searchBST(root.left, val)
            else: return self.searchBST(root.right, val)

        return None

######################################################

#   Iterative Approach

#   Runtime: 73ms   -   92.99%
#   Memory: 16.4MB  -   96.41%

######################################################

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        while root:
            if root.val == val: return root
            if val < root.val: root = root.left
            else: root = root.right

        return None