# 116. Populating Next Right Pointers in Each Node

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        if not root:
            return root
        
        q = deque([])
        q.append(root)
        
        while(q):
            
            l = deque([])
            
            while(q):
                node = q.popleft()
                
                if node.left:
                    l.append(node.left)
                if node.right:
                    l.append(node.right)

                if q:
                    node.next = q[0]
            
            q = q + l
        return root
            
        
