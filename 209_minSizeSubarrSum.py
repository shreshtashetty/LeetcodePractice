# 209. Minimum Size Subarray Sum

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        l = len(nums)+1
        
        left, right = 0, 0
        
        sub_sum = nums[left]
        
        while left<=right and right<len(nums):
            if sub_sum>=target:
                while(sub_sum>=target):
                    l = min(l, right-left+1)
                    sub_sum-=nums[left]
                    left+=1
                
            else:
                right+=1
                if right<len(nums):
                    sub_sum+=nums[right]
                
                
        return l if l < len(nums)+1 else 0
