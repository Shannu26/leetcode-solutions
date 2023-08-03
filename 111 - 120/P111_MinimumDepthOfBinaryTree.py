######################################################

#   Solved on Saturday, 22 - 01 - 2022.

######################################################


######################################################

#   Recursive Solution

#   Runtime: 564ms   -   73.45%
#   Memory: 50.5MB  -   60.45%

######################################################

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        def traverse(root):
            if root: 
                # If root is leaf node, we return 1
                if root.left == None and root.right == None: return 1
                leftDepth = traverse(root.left)
                # If left subtree has min depth 1, then right subtree can't beat it
                # because right subtree will have height starting from 1, but not 0
                if leftDepth == 1: return 2
                rightDepth = traverse(root.right)
                # If right subtree has min depth 1, then left subtree can't beat it
                # because left subtree will have height starting from 1, but not 0
                if rightDepth == 1: return 2
                return min(leftDepth, rightDepth) + 1
            # Since we need min depth, for empty node, we return inf instead of 0
            return math.inf
        
        depth = traverse(root)
        return depth if depth != math.inf else 0

######################################################

#   Iterative Solution

#   Runtime: 484ms   -   86.94%
#   Memory: 48.8MB  -   98.72%

######################################################

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # Why it is faster than recursive method is, we return from the functoon
        # here when we find the first leaf node. Whereas in recursive method
        # solution building start from the leaf node, so mostly we need to traverse
        # all nodes in recursive method which is eliminated in iterative appraoch
        if not root: return 0
        
        queue = [root]
        depth = 1
        # Number of nodes in current level. Currently we have only root
        size = 1
        # Number of nodes in next level. 0 since we haven't traversed the tree
        nextSize = 0
        
        while queue:
            node = queue.pop(0)
            # Since we visited node at start of queue, we reduce size by 1
            size -= 1
            # If node is leaf node, it will be the first leaf node we encountered, since
            # we are returning from func in this condition. So, since it is the
            # first leaf node, the depth from root will be min till this node which is
            # store in depth. So we return it
            if node.left == None and node.right == None: return depth
            # If node.left is not none we add it to queue and increase nextSize
            if node.left: 
                queue.append(node.left)
                nextSize += 1
            # If node.right is not none we add it to queue and increase nextSize
            if node.right: 
                queue.append(node.right)
                nextSize += 1
            # Size will be 0 if we visited all nodes in current level. So we move on
            # to next level, by assigning nextSize to size, changing neztSize to 0
            # and moving to next level, by increasing depth by 1
            if size == 0:
                size = nextSize
                nextSize = 0
                depth += 1

