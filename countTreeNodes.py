# 222. Count Complete Tree Nodes

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def count(root, num):
    
    if not root:
        return 0
    
    left = count(root.left, num)
    right = count(root.right, num)

    num+=left+right
    
    return num

    
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        
        num = 1
        num = count(root, num)
        return num
        
