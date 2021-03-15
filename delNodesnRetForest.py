# https://www.youtube.com/watch?v=aaSFzFfOQ0o&list=PLi9RQVmJD2fapKJ4DnZzAn55NJfo5IM1c&index=54

# Definition for a binary tree node.
# 1110. Delete Nodes And Return Forest

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def removeNodes(root, to_delete, remaining):
    if not root:
        return None
    
    root.left = removeNodes(root.left, to_delete, remaining)
    root.right = removeNodes(root.right, to_delete, remaining)
    
    if root.val in to_delete:
        if root.left:
            remaining.append(root.left)
        if root.right:
            remaining.append(root.right)
        root = None
    return root
    

class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        remaining = []
        toDelete = set()
        for i in range(len(to_delete)):
            toDelete.add(to_delete[i])
            
        root = removeNodes(root, toDelete, remaining)
        if(root and root not in toDelete):
            remaining.append(root)
        
        return remaining
    
    
        
        
