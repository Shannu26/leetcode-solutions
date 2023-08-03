######################################################

#   Solved on Wednesday, 12 - 01 - 2022.

######################################################


######################################################

#   Runtime: 48ms   -   93.03%
#   Memory: 14.5MB  -   98.93%

######################################################

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        """
            Logic is, we traverse the tree recursively and we set leaf node's value
            to -1 if it currently has target value.
            Upon reaching a node after traversing its children, we check whether
            left or right node has -1, then that means that node is a leaf node
            with target as val. So we set root.left or root.right to None.
            Then we check if current root node is a leaf node and if its value is 
            target we set its value to -1
        """
        def traverse(root):
            if not root: return
            traverse(root.left)
            traverse(root.right)
            # If left node is leaf node with target as its value, it will have -1
            # after recursive calls. So, we set root.left to None
            if root.left and root.left.val == -1: 
                root.left = None
            # If right node is leaf node with target as its value, it will have -1
            # after recursive calls. So, we set root.right to None
            if root.right and root.right.val == -1: 
                root.right = None
            # Checking if root node is leaf node with target as val. If yes, setting
            # root.val to -1
            if not root.left and not root.right and root.val == target:
                root.val = -1
        
        traverse(root)
        # If root.val is -1, that means all nodes in the given tree have target as 
        # value because tree has only positive values. So, we return None
        if root.val == -1: return None
        # Else, return root
        return root