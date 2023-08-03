######################################################

#   Solved on Friday, 15 - 04 - 2022.

######################################################


######################################################

#   Runtime: 45ms   -   96.40%
#   Memory: 18MB  -   83.03%

######################################################


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if root:
            # Since given tree is BST, if root.val < low, we can say that all nodes
            # to left of root are < root.val => < low, so, we can remove left subtree
            # of root. So, we trim right subtree recursively and store that result in
            # root
            if root.val < low:
                root = self.trimBST(root.right, low, high)
            # Since given tree is BST, if root.val > high, we can say that all nodes
            # to right of root are > root.val => > high, so, we can remove right subtree
            # of root. So, we trim left subtree recursively and store that result in
            # root
            elif root.val > high:
                root = self.trimBST(root.left, low, high)
            # root node is valid since low < root.val < high. So we recursively
            # trim left and right subtrees and store them in respective root's left 
            # and right pointer
            else:
                root.left = self.trimBST(root.left, low, high)
                root.right = self.trimBST(root.right, low, high)
            # Returning root
            return root
        return None