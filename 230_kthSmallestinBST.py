# 230. Kth Smallest Element in a BST

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def traverse(root, l):
    if not root:
        return 
    l.append(root.val)
    traverse(root.left,l)
    traverse(root.right,l)
    return l
    

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
#         BRUTE FORCE
#         l = []
#         l = traverse(root, l)
#         l = sorted(l)
#         return l[k-1]

#       THEIR SOLUTION
        def inorder(r):
            return inorder(r.left) + [r.val] + inorder(r.right) if r else []
    
        return inorder(root)[k - 1]
