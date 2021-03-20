# 783. Minimum Distance Between BST Nodes

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import numpy as np

class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        def findDiff(root):
            
            nonlocal l
            if not root:
                return None
            
            left = findDiff(root.left)
            l.append(root.val)
            right = findDiff(root.right)
            
            return root
        
        
        l = []
        node = findDiff(root)
        print(l)
        l.sort()
        min_dist = np.inf
        for i in range(1, len(l)):
            if min_dist>l[i]-l[i-1]:
                min_dist = l[i]-l[i-1] 
        return min_dist
        
        
#     def findDiff(root):
#             nonlocal min_dist
#             if not root:
#                 return None

#             left = findDiff(root.left)
#             if left:
#                 diff1 = abs(root.val-left.val)
#                 if diff1<min_dist:
#                     min_dist = diff1

#             # print(root.val)

#             right = findDiff(root.right)
#             if right:
#                 diff2 = abs(root.val-right.val)
#                 if diff2<min_dist:
#                     min_dist = diff2
#             print(min_dist)
#             return root
