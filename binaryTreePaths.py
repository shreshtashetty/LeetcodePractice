# 257. Binary Tree Paths

# Refer to Nick White's Video https://www.youtube.com/watch?v=H2D4HcVZq_g

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def traverse(root, current, result):
        current += "->" + str(root.val)
        
        if not root.left and not root.right:
            result.append(current)
            return
        if root.left:
            traverse(root.left, current, result)
        if root.right:
            traverse(root.right, current, result)

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        result = []
        if not root:
            return result
        current_path = str(root.val)
        if not root.left and not root.right:
            result.append(current_path)
        if root.left:
            traverse(root.left, current_path, result)
        if root.right:
            traverse(root.right, current_path, result)
        return result
