# 662. Maximum Width of Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        
        if not root.left and not root.right:
            return 1
        
        q = [(root,0)]
        width = 1
        
        while q:
            if len(q)>1:
                width = max(width, q[-1][1]-q[0][1]+1)
                
            temp_q = []
            while q:
                node, position = q.pop(0)
                if node.left:
                    temp_q.append((node.left, 2*position))
                if node.right:
                    temp_q.append((node.right, 2*position+1))
                    
            q = temp_q
            
        return width
