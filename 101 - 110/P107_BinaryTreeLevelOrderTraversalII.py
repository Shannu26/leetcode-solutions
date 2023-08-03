######################################################

#   Solved on Wednesday, 12 - 01 - 2022.

######################################################


######################################################

#   Runtime: 20ms   -   99.90%
#   Memory: 14.4MB  -   93.32%

######################################################

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        # We will do a BFS
        if not root: return []
        # stack for the Iterative BFS
        stack = [root]
        # levelOrder has the required result
        levelOrder = []
        # Since at level 1 only root is present, we initialize with 1
        currentCapacity = 1
        # Since we haven't started traversing tree, we initialize with 0
        nextCapacity = 0
        # It stores the values in next level
        nextLevel = []
        
        while stack:
            # We visited the node at start of stack
            node = stack.pop(0)
            # So, we reduce the currentCapacity by 1
            currentCapacity -= 1
            # We add current node val to nextLevel
            nextLevel.append(node.val)
            # If node has left child, we add it to stack and increase nextCapacity by 1
            if node.left: 
                stack.append(node.left)
                nextCapacity += 1
            # If node has right child, we add it to stack and increase nextCapacity by 
            # 1
            if node.right: 
                stack.append(node.right)
                nextCapacity += 1
            # If currentCapacity is 0, that means we traversed all nodes at current
            # level
            if currentCapacity == 0:
                # So, we change val in nextCapacity to currentCapacity and nextCapacity
                # to 0
                currentCapacity = nextCapacity
                nextCapacity = 0
                # We add nextLevel nodes to levelOrder list and we change nextLevel
                # to empty list for next level
                levelOrder.append(nextLevel[:])
                nextLevel = []
        # We return the reverse of levelOrder, since we need levelOrder in bottom-up
        # manner and we currently have top-dowm manner
        return levelOrder[::-1]
