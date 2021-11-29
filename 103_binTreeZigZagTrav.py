# 103. Binary Tree Zigzag Level Order Traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# For a less hacky solution, follow https://www.youtube.com/watch?v=4Z8mqw7lWWc

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        
        direction = 1 # flag is 1 for left to right and -1 for right to left
        stack = deque()
        result = []
        
        if not root:
            return None
        stack.append((root, 1))
        
        while stack:
            
            curr, j = stack.popleft()
            
            if curr.left: stack.append((curr.left, j+1))
            if curr.right: stack.append((curr.right, j+1))
            
            if len(result)<j:
                result.append([curr.val])
            else:
                result[-1].append(curr.val)
        
        for i in range(len(result)):
            if(direction == 1):
                pass
            else:
                result[i] = result[i][::-1]
            direction*=-1
                
        return result
