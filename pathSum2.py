# 113. Path Sum II

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# To do it with lists instead of strings, pass a copy of the list during recursion.
# More deets on https://www.youtube.com/watch?v=3B5gnrwRmOA&list=PLi9RQVmJD2fZgRyOunLyt94uVbJL43pZ_&index=28
def path(root, targetSum, l, v):
    if root.left is None and root.right is None and targetSum-root.val==0:
        l+=str(root.val)
        # print(l)
        v.append(l)
        # print(v)
        
    l+=str(root.val)+"_"
    targetSum-=root.val
    if root.left:
        path(root.left, targetSum, l, v)
    if root.right:
        path(root.right, targetSum, l, v)
 
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        if root is None:
            return []
        l = ""
        v = []
        path(root, targetSum, l, v)
        
        for i in range(len(v)):
            v[i] = v[i].split("_")
            for j in range(len(v[i])):
                v[i][j] = int(v[i][j])
      
        return v
        
