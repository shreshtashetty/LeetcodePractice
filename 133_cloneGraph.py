# 133. Clone Graph

# Neetcode: https://www.youtube.com/watch?v=mQeF6bN8hMk

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        oldToNew = {}
        
        def clone(node):
  
            if node in oldToNew:
                return oldToNew[node]
            
            copy = Node(node.val)
            oldToNew[node] = copy
            
            for i in range(len(node.neighbors)):
                copy.neighbors.append(clone(node.neighbors[i]))
                
            return copy
        
        return clone(node) if node else None
        
            
        
