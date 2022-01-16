# 98. Validate Binary Search Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        l = []
        
        def inorder(root):
            if not root:
                return
            
            inorder(root.left)
            l.append(root.val)
            inorder(root.right)
            
        inorder(root)
        
        if l!=sorted(l):
            return False
        else:
            for i in range(1,len(l)):
                if l[i-1]==l[i]:
                    return False
            return True
