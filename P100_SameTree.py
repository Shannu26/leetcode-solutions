######################################################

#   Solved on Tuesday, 04 - 01 - 2022.

######################################################


######################################################

#   Runtime: 24ms   -   95.57%
#   Memory: 14MB  -   99.72%

######################################################


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # We are using recursion to solve this problem

        # This is the base case. If both trees are none, we return True
        if not p and not q: return True
        # If either of 2 trees is None, that means they are not same trees. So we
        # return False
        if not q or not p : return False
        # If value present at current node of trees are not equal, that means trees
        # are not same. So we return False
        if p.val != q.val: return False
        # We recursively check for left and right nodes of trees p,q and return "and"
        # of both results. Why "and" is, both left and right subtrees should be same
        # if the current trees has to be same
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)