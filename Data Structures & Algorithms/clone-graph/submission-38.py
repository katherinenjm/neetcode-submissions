"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return None
        
        oldToNew = {}   # mapping: original node -> clone
        
        def dfs(original):
            print(f"for node.val = {original.val}, ")
            if original in oldToNew:
                return oldToNew[original]
            # create clone, store it, then recursively clone neighbors
            copy = Node(original.val)
            oldToNew[original] = copy
            for neighbor in original.neighbors:
                copy.neighbors.append(dfs(neighbor))
            return copy
            # ...
        
        return dfs(node)






        