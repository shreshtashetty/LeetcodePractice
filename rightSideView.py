# 199. Binary Tree Right Side View

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Done using BFS

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        visible_nodes = []
        q = deque([])
        if not root:
            return visible_nodes
        
        q.append(root)
        
        while q:
            size = len(q)
            for i in range(size):
                current = q.popleft()
                if i==size-1: # last element of the queue will be the "visible element"
                    visible_nodes.append(current.val)
                if current.left:
                    q.append(current.left)
                if current.right:
                    q.append(current.right)
        return visible_nodes
       
