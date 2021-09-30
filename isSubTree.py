# 572. Subtree of Another Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def check(root, subRoot):
    if not root and subRoot:
        return False
    if root and not subRoot:
        return False
    if not root and not subRoot:
        return True
    if root and subRoot:
        if root.val != subRoot.val:
            return False
        elif root.val == subRoot.val:
            left = check(root.left, subRoot.left)
            right = check(root.right, subRoot.right)
            if left and right:
                return True

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return None
        c = check(root, subRoot)
        if c:
            return True
        else:
            left = self.isSubtree(root.left, subRoot)
            right = self.isSubtree(root.right, subRoot)
            if left or right:
                return True
            else:
                return False
        
        
