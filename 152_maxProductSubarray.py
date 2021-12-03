# 152. Maximum Product Subarray

# Modification of Kadane's Algorithm

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        global_max = prev_max = prev_min = nums[0]
        
        for x in nums[1:]:
            
            local_max = max(prev_max*x, prev_min*x, x)
            local_min = min(prev_max*x, prev_min*x, x)
            
            global_max = max(global_max,local_max)
            
            prev_max, prev_min = local_max, local_min
            
        return global_max
