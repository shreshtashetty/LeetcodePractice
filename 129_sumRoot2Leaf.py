# 129. Sum Root to Leaf Numbers

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def dfs(root, num):
    
    if not root:
        return 0
    
    num = num*10 +root.val
    
    if not root.left and not root.right:
        return num
    
    return dfs(root.left, num)+dfs(root.right, num)
    
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        
        return dfs(root, 0)
