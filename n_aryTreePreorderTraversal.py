#589. N-ary Tree Preorder Traversal
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        nodeStack = []
        nodeStack.append(root)
        
        if(root==None):
            return []
        
        l = []
        while(len(nodeStack)>0):
            node = nodeStack.pop()
            l.append(node.val)
            
            if(node.children is not None):
                for i in range(len(node.children)-1, -1, -1):
                    nodeStack.append(node.children[i])
        return l
            
        
