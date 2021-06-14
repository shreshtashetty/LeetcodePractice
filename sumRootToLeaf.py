# 1022. Sum of Root To Leaf Binary Numbers

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def traverse(root, l, num):
    if root.left is None and root.right is None:
        l.append(num+str(root.val))
        return
    
    num += str(root.val)
    if root.left:
        left = traverse(root.left, l, num)
    if root.right:
        right = traverse(root.right, l, num)
    
    
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        l = []
        num = ''
        traverse(root, l, num)
        sum_ = 0
        for i in l:
            sum_+=int(i, base=2)
        
        return sum_
        
        
        
