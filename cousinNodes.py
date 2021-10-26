# 993. Cousins in Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        
        # areCousins = False
        
        q1 = deque([])
        q2 = deque([])
        
        q1.append(root)
        q2.append(root.val)
        
        while(q1):
            for _ in range(len(q1)):
                node = q1.popleft()
                q2.popleft()
                if node.left:
                    q1.append(node.left)
                    q2.append((node.left.val, node.val))
                if node.right:
                    q1.append(node.right)
                    q2.append((node.right.val, node.val))
            ind1 = 0
            ind2 = 0

            for i in range(len(q2)):
                if x == q2[i][0]:
                    ind1 = q2[i][1]
                if y == q2[i][0]:
                    ind2 = q2[i][1]
                if ind1!=ind2 and ind1>0 and ind2>0:
                    return True
            
        return False
        
        
        
        
