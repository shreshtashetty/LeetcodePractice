# 110. Balanced Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def getHeight(root):
    if(root==None):
        return -1 # height
    height = 0
    height1 = getHeight(root.left)
    height2 = getHeight(root.right)

    height+= max(height1,height2) + 1

    return height

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if root==None:
            return True

        if(abs(getHeight(root.left)-getHeight(root.right))>1):
            return False
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
