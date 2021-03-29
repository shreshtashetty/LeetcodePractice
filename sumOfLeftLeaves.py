# 404. Sum of Left Leaves

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        sum_left = 0
        
        def traverse(root):
            
            nonlocal sum_left
            
            if root is None:
                return None

            left = traverse(root.left)
            if left:
                if not left.left and not left.right:
                    sum_left+=left.val
            right = traverse(root.right)

            return root
        
        node = traverse(root)
        return sum_left
        
