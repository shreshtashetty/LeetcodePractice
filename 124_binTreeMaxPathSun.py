# 124. Binary Tree Maximum Path Sum

# Neetcode: https://www.youtube.com/watch?v=Hr5cWUld4vU

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]
        
        def dfs(root):
            if not root:
                return 0
            
            leftmax = dfs(root.left)
            rightmax = dfs(root.right)
            
            # Max path with splitting
            left = max(leftmax,0)
            right = max(rightmax,0)
            
            res[0] = max(res[0], root.val+left+right)
            
            # Max path without splitting
            return root.val+max(left,right)
        
        dfs(root)
        
        return res[0]
