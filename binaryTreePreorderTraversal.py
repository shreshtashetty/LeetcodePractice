#144. Binary Tree Preorder Traversal
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # l = []
        # if(root):
        #     l.append(root.val)
        #     l+=self.preorderTraversal(root.left)
        #     l+=self.preorderTraversal(root.right)
        # return l
        nodeStack = [] 
        nodeStack.append(root) 
  
    #  Pop all items one by one. Do following for every popped item 
    #   a) print it 
    #   b) push its right child 
    #   c) push its left child 
    # Note that right child is pushed first so that left 
    # is processed first */ 
        if(root is None):
            return []
        l = []
        while(len(nodeStack) > 0): 
            # Pop the top item from stack and print it 
            node = nodeStack.pop() 
            l.append(node.val) 
          
            # Push right and left children of the popped node 
            # to stack 
            if node.right is not None: 
                nodeStack.append(node.right) 
            if node.left is not None: 
                nodeStack.append(node.left) 
        return l
