#590. N-ary Tree Postorder Traversal
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        # l = []
        # if(root is None):
        #     return []
        # if(root.children is not None):
        #     for i in range(len(root.children)):
        #         if(root.children[i].val is not None):
        #             l.extend(self.postorder(root.children[i]))
        # l.append(root.val)
        # return l
        
        if(root is None):
            return []
        
        nodeStack = []
        nodeStack.extend(root.children)
        l = []
        while(len(nodeStack)>0):
            node = nodeStack.pop(0)
            l.append(node.val)
            for i in range(len(node.children)-1, -1, -1):
                if(node.children[i] is not None):
                    nodeStack.append(node.children[i])
        l.append(root.val)
        return l
