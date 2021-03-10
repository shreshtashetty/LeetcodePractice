# 100. Same Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def Traverse(l, root):
    if(root==None):
        return None, l.append(None)
    l.append(root.val)
    left = Traverse(l, root.left)
    right = Traverse(l, root.right)
    
    return root, l
    

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if(p==None and q==None):
            return True
        if(p==None and q!=None):
            return False
        if(q==None and p!=None):
            return False
        l1 = []
        l2 = []
        p1, l1 = Traverse(l1, p)
        p2, l2 = Traverse(l2, q)
        
        if(l1==l2):
            return True
        else:
            return False
        
        
