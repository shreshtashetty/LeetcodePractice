# 938. Range Sum of BST
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def sumRange(root, low, high, sum_):
    if not root:
        return sum_
    
    if root.val>=low and root.val<=high:
        sum_+=root.val
    
    sum_ = sumRange(root.left, low, high, sum_)
    sum_ = sumRange(root.right, low, high, sum_)
    
    return sum_
    

class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        
        return sumRange(root, low, high, 0)
