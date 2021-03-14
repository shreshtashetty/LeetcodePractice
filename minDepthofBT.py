# 111. Minimum Depth of Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        
        if not root:
            return 0
        
        q = deque()
        q.append((root, 1))
        
        while(q):
            node, depth = q.popleft()
            if node.left or node.right:
                depth+=1
                if node.left:
                    q.append((node.left, depth))
                if node.right:
                    q.append((node.right, depth))  
            else:
                break

        return depth
            
            
        
