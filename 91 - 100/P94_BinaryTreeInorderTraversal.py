######################################################

#   Solved on Wednesday, 05 - 01 - 2022.

######################################################


######################################################

#   Approach I : Using Recursion

#   Runtime: 24ms   -   95.86%
#   Memory: 14MB  -   92.19%

######################################################

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        
        inorder = []
        
        def traverse(root):
            if root:
                traverse(root.left)
                inorder.append(root.val)
                traverse(root.right)
                
        traverse(root)
        return inorder


######################################################

#   Approach II : Without Recursion

#   Runtime: 24ms   -   95.86%
#   Memory: 14MB  -   92.19%

######################################################

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        
        inorder = []
        stack = []
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            
            node = stack.pop()
            inorder.append(node.val)
            node = node.right
        
        return inorder
        