# 145. Binary Tree Postorder Traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        # l = []
        # if(root):
        #     l+=self.postorderTraversal(root.left)
        #     l+=self.postorderTraversal(root.right)
        #     l.append(root.val)
        # return l
#---------------------------------------------------------------------------------        
        # 1. Push root to first stack.
        # 2. Loop while first stack is not empty
        #     2.1 Pop a node from first stack and push it to second stack
        #     2.2 Push left and right children of the popped node to first stack
        # 3. Print contents of second stack
        
        nodeStack1 = []
        nodeStack2 = []
        nodeStack1.append(root)
        # print(root)
        
        if root==None:
            return None
        
        while(nodeStack1):
            node = nodeStack1.pop()
            nodeStack2.append(node.val)
            if(node.left!=None):
                nodeStack1.append(node.left)
            if(node.right!=None):
                nodeStack1.append(node.right)
        # print(nodeStack1, nodeStack2)
        
        nodeStack2.reverse()
        
        return nodeStack2
            
