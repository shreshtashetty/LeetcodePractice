# 213. House Robber II

'''
Since House[1] and House[n] are adjacent, they cannot be robbed together. 
Therefore, the problem becomes to rob either House[1]-House[n-1] or House[2]-House[n], 
depending on which choice offers more money. 
Now the problem has degenerated to the House Robber, which is already been solved.
'''

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums)<3:
            return max(nums)
        
        nums1 = nums[:-1].copy()
        nums2 = nums[1:].copy()
        
        for i in range(len(nums1)-3, -1, -1):
            nums1[i] = nums1[i]+max(nums1[i+2:])
            
        for i in range(len(nums2)-3, -1, -1):
            nums2[i] = nums2[i]+max(nums2[i+2:])
        
        # print(nums1, nums2)
        
        return max(nums1+nums2)
            
