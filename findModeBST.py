# 501. Find Mode in Binary Search Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def Mode(root, d, max_):
    if root is None:
        return 
    if root.val not in d:
        d[root.val]=1
    else:
        d[root.val]+=1
        
    if max_[0]<d[root.val]:
        max_[0] = d[root.val]
    left = Mode(root.left, d, max_)
    right = Mode(root.right, d, max_)
    
    return d, max_
    

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        d, max_ = Mode(root, d={}, max_=[0])
        l = []
        for keys, values in d.items():
            if values==max_[0]:
                l.append(keys)
        return l
        
        
        
        
