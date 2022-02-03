# 1302. Deepest Leaves Sum

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def maxDepth(root, depth):
    
    if not root:
        return depth
    
    left = 1+maxDepth(root.left, depth)
    right = 1+maxDepth(root.right, depth)
    
    depth = max(left, right)
    
    return depth

def findSum(root, depth, sum_leaves):
    
    if root and depth==1:
        sum_leaves+=root.val
        return sum_leaves
    
    if not root and depth>1:
        return 0
    
    if root:
        depth-=1
        
        left = findSum(root.left, depth, sum_leaves)
        right = findSum(root.right, depth, sum_leaves)
        
        sum_leaves = left+right
        
    return sum_leaves
        

class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        
        depth = 0
        depth = maxDepth(root, depth)
        sumLeaves = 0
        sumLeaves = findSum(root, depth, sumLeaves)

        return sumLeaves
        
