######################################################

#   Solved on Friday, 21 - 01 - 2022.

######################################################


######################################################

#   Time Optimized Solution

#   Runtime: 40ms   -   98.81%
#   Memory: 19.2MB  -   25.27%

######################################################

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def traverse(root):
            """
                Input: 
                    Node of a Tree
                Output:
                    (isBalanced, height)
                    isBalanced is a boolean value that determines whether tree
                    having root as given input is balanced or not

                    height is the height of the tree having root as given input
            """
            if root:
                # Recursively calling left and right subtrees, to solve those sub
                # problems
                left = traverse(root.left)
                right = traverse(root.right)
                # If any of the left or right subtrees are not balanced, tree is
                # not balanced. So, we return (False, -1)
                if not(left[0] and right[0]): return (False, -1)
                # If tree is balanced it will have abs(leftHeight - rightHeight)
                # between -1 and 1
                return (-1 <= left[1] - right[1] <= 1, max(left[1], right[1]) + 1)
            # If root is None, there is no tree, so height will be 0. Since tree is
            # None, it can be treated as balanced. So we return (True, 0)
            return (True, 0)
        
        return traverse(root)[0]

######################################################

#   Optimized Solution

#   Runtime: 36ms   -   99.77%
#   Memory: 18.9MB  -   52.35%

######################################################

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # In this approach instead of having isBalanced as an output value which
        # increases space complexity, we use a nonlocal variable
        balanced = True
        
        def traverse(root):
            # This func is same as func we use to find height of tree, with only
            # change of updating the nonlocal balance variable
            nonlocal balanced
            
            if root:
                left = traverse(root.left)
                right = traverse(root.right)
                # Updating the nonlocal balanced variable
                balanced = balanced and (-1 <= left - right <= 1)
                return max(left, right) + 1
            
            return 0
        
        traverse(root)
        return balanced