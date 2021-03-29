# 563. Binary Tree Tilt

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def findSum(root):
    sum_ = 0
        
    def sumUpVals(root):

        nonlocal sum_

        if not root:
            return None

        left = sumUpVals(root.left)
        sum_ += root.val
        right = sumUpVals(root.right)

        return root
    node = sumUpVals(root)
    return sum_

def tilt(root):
    if not root.left and not root.right:
        return 0
    else:
        if root.left:
            sumleft = findSum(root.left)
        else:
            sumleft = 0

        if root.right:
            sumright = findSum(root.right)
        else:
            sumright = 0

    return abs(sumleft - sumright)


class Solution:
    def findTilt(self, root: TreeNode) -> int:
        total_tilt = 0
        
        def findTilt_(root):
            
            nonlocal total_tilt
            
            if not root:
                return None
            
            left = findTilt_(root.left)
            t = tilt(root)

            total_tilt = total_tilt+t

            right = findTilt_(root.right)
            return root
        
        node = findTilt_(root)
        
        return total_tilt
        
        
        
        
