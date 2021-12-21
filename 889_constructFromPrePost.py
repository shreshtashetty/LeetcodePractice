# 889. Construct Binary Tree from Preorder and Postorder Traversal

# Got from solution in discuss section.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        root = TreeNode(postorder.pop())
        if len(preorder) == 1:
            return root
        rightIndex = preorder.index(postorder[-1])
        root.right = self.constructFromPrePost(preorder[rightIndex:], postorder)
        root.left = self.constructFromPrePost(preorder[1:rightIndex], postorder)
        return root
