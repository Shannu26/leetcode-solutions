######################################################

#   Solved on Tuesday, 01 - 02 - 2022.

######################################################


######################################################

#   Runtime: 308ms   -   85.10%
#   Memory: 16MB  -   87.78%

######################################################

class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        # Stores the nodes that are already visited
        visited = set()
        # Stores the roots of the trees
        roots = set()
        
        def bfs(startNode):
            # BFS traversal starting at startNode
            queue = [startNode]

            while queue:
                # Getting next node
                node = queue.pop(0)
                # If node is already visited
                if node in visited:
                    # but node is not a root in previous iterations then, given 
                    # nodes form a graph, not a tree since tree has ony 1 parent for
                    # each node. So we return False
                    if node not in roots: return False
                    # If node is root in previous iterations then we found out that
                    # node has a parent and it is not actually a root. So we remove
                    # it from roots and skip this iteration
                    roots.remove(node)
                    continue
                # Adding node to visited
                visited.add(node)
                # If left child is present, add it to queue
                if leftChild[node] != -1: 
                    queue.append(leftChild[node])
                # If right child is present, add it to queue
                if rightChild[node] != -1: 
                    queue.append(rightChild[node])
            # We will reach here only if the tree having startNode as root is not
            # a graph. So we return True
            return True
        
        for node in range(n):
            # If node is not visited, then we do a bfs search considering node as
            # root to find the subtree that starts with node as root
            # This node might be the actual root node or might be a subtree
            # So, we add it to roots set after the bfs traversal since hoping
            # that in next iterations a node which is a parent of this node
            # will appear and then it will remove this node from the roots set
            if node not in visited:
                # BFS function will return False if we find a node in the traversal
                # which is already visited. If that happens it is not a tree
                # since a tree has only 1 parent for each node. So  we return False
                if not bfs(node): return False
                # Since we are considering node as root, adding it to roots
                roots.add(node)
        # If given nodes form a single valid tree, roots set will finally have only
        # 1 node in it. If it has > 1 node that means the given nodes form multiple
        # disconnected trees. So we return True if len(roots) == 1. Else we return 
        # False
        return len(roots) == 1