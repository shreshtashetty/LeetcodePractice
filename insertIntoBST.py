# 701. Insert into a Binary Search Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if(root==None):
            return TreeNode(val)
        if(val>root.val):
            node = self.insertIntoBST(root.right, val)
            root.right = node
        if(val<root.val):
            node = self.insertIntoBST(root.left, val)
            root.left = node
 
        return root
            
