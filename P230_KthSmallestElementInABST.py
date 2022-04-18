######################################################

#   Solved on Monday, 18 - 04 - 2022.

######################################################


######################################################

#   Iterative Approach

#   Runtime: 45ms   -   96.55%
#   Memory: 17.9MB  -   99.08%

######################################################

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Inorder traversal
        stack = [root]
        node = root
        kValue = 0
        
        while True:
            while node:
                stack.append(node)
                node = node.left
            
            if stack:
                node = stack.pop()
                kValue += 1

                if kValue == k: return node.val
                node = node.right

######################################################

#   Recursive Approach

#   Runtime: 45ms   -   96.55%
#   Memory: 17.9MB  -   99.08%

######################################################

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Inorder traversal
        kValue = 0
        kthMinimum = -1
        
        def traverse(root):
            nonlocal kValue
            nonlocal kthMinimum
            if root:
                traverse(root.left)
                kValue += 1
                if kValue == k: kthMinimum = root.val
                traverse(root.right)
        
        traverse(root)
        return kthMinimum