#94. Binary Tree Inorder Traversal
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:

#       1) Create an empty stack S.
#       2) Initialize current node as root
#       3) Push the current node to S and set current = current->left until current is NULL
#       4) If current is NULL and stack is not empty then 
#           a) Pop the top item from stack.
#           b) Print the popped item, set current = popped_item->right 
#           c) Go to step 3.
#       5) If current is NULL and stack is empty then we are done.

        l = []
        t = []
        current = root
        # print(root)
        while(True):
            while(current!=None):
                l.append(current)
                current = current.left
        
            if(current==None and l!=[]):
                n = l.pop()
                t.append(n.val)
                current = n.right
                
            elif(current==None and l==[]):
                break
        
        return t
        
