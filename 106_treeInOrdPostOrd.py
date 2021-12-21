# 106. Construct Binary Tree from Inorder and Postorder Traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#   MY UNCLEAN BUT FASTER SOLUTION

# def build(inorder, postorder, checked):
    
#     if not inorder:
#         return None
    
#     root = TreeNode(postorder[-1])
#     mid = inorder.index(postorder[-1])
#     checked.add(postorder[-1])
    
#     root.right = build(inorder[mid+1:], postorder[:-1], checked)
    
#     while postorder[-1] in checked:
       
#         postorder.pop(-1)
#         if not postorder:
#             break
    
#     root.left = build(inorder[:mid], postorder, checked)
   
#     return root

# class Solution:
#     def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
#         checked = set()
#         root = build(inorder, postorder, checked)
#         return root
        
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        # A CLEANER LOOKING SOLUTION
        
        if not inorder or not postorder:
            return None
    
        root = TreeNode(postorder[-1])
        mid = inorder.index(postorder[-1])
        
        root.left = self.buildTree(inorder[:mid], postorder[:mid])
        root.right = self.buildTree(inorder[mid+1:], postorder[mid:-1])

        return root

