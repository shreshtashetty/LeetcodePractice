# 101. Symmetric Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def mirrored(t1, t2):
    if t1 is None and t2 is None:
        return True
    if t1 is None and t2 is not None:
        return False
    if t2 is None and t1 is not None:
        return False
    
    return (t1.val==t2.val) and mirrored(t1.right, t2.left) and mirrored(t1.left, t2.right)

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return mirrored(root, root)
        
