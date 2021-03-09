# 102. Binary Tree Level Order Traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# INPUT: [3,9,20,null,null,15,7]

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        
        # BFS GIVING [[3],[9,20],[15,7]] AS OUTPUT

        # DEQUE STORING NODES AND LEVEL NUMBER. 
        # RESULT STORING VALUES. UPDATES ACCORDING TO THE LEVEL NUMBER.
        
        if not root: return []
        result, q = [], deque([(root, 1)]) # result = values, deque = nodes, level no.
        
        while q:
            curr, j = q.popleft()
            
            if curr.left: q.append((curr.left, j + 1))
            if curr.right: q.append((curr.right, j + 1))
                
            if len(result) < j: result.append([curr.val])
            else: result[-1].append(curr.val)
            
        return result
    
    
#         # NORMAL BFS GIVING SINGLE LIST OF VALUES AS OUTPUT
#         # I.E., BFS GIVING [3,9,20,15,7]
#         nodeStack = []
#         l = []
#         if(root==None):
#             return None
#         else:
#             nodeStack.append(root)
        
#         while(nodeStack):
#             node = nodeStack.pop(0)
#             l.append(node.val)
#             if(node.left!=None):
#                 nodeStack.append(node.left)
#             if(node.right!=None):
#                 nodeStack.append(node.right)
#         print(l)        
#         return l
