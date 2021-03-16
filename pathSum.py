# 112. Path Sum

# https://www.youtube.com/watch?v=Hg82DzMemMI
# Subtract the root.val from the sum at each level recursively and check if you reach 0 sum at any leaf.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def hasPathSum(self, root: TreeNode, s: int) -> bool:
        if not root:
            return False
        elif not root.left and not root.right and s-root.val==0:
            return True
        else:
            return self.hasPathSum(root.left,s-root.val) or self.hasPathSum(root.right,s-root.val)
            
