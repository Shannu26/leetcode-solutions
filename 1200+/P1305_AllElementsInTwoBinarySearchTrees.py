######################################################

#   Solved on Wednesday, 26 - 01 - 2022.

######################################################


######################################################

#   Runtime: 333ms   -   79.64%
#   Memory: 22.4MB  -   45.36%

######################################################

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        
        elements = []
        # Inorder traversal
        def traverse(root):
            if root:
                traverse(root.left)
                elements.append(root.val)
                traverse(root.right)
        # Performing inorder traversal on both trees and storing them in elements
        traverse(root1)
        traverse(root2)
        # Sorting elements array and returning it
        return sorted(elements)