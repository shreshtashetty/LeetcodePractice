# 643. Maximum Average Subarray I

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        max_sum = sum(nums[:k])/k
        sum_ = max_sum
        
        for i in range(1, len(nums)-k+1):
            sum_ = (sum_*k - nums[i-1] + nums[i+k-1])/k
            max_sum = max(max_sum, sum_)
            
        return max_sum
