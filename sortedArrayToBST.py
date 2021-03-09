# 108. Convert Sorted Array to Binary Search Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Referred to Nick White's Video.
#Worked it in a way similar to Binary Search

def buildBST(nums, left, right):
    if(left>right):
        print(left, right)
        return None
    mid = int(left + (right-left)/2)
    root = TreeNode(nums[mid], buildBST(nums, left, mid-1), buildBST(nums, mid+1, right))
    return root
    
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if(len(nums)==0):
            return None
        return buildBST(nums, 0, len(nums)-1)
        
