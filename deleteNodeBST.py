# 450. Delete Node in a BST

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# https://www.youtube.com/watch?v=i2s4Tyw3_dY

def findMin(root):
    while root.left:
        root = root.left
    return root

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return root

        elif key<root.val:
            root.left = self.deleteNode(root.left, key)

        elif key>root.val:
            root.right = self.deleteNode(root.right, key)

        else:
            # For a leaf node
            if not root.left and not root.right:
                root = None

            
            # For a not with only 1 child
            elif not root.left:
                root = root.right

            
            elif not root.right:
                root = root.left

                
            # For a node with 2 children
            else:
                temp = findMin(root.right)
                root.val = temp.val
                root.right = self.deleteNode(root.right, temp.val)

        return root
