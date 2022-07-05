# 2090. K Radius Subarray Averages

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        
        if k==0:
            return nums
        
        ans = []
        
        ans = [-1]*len(nums)
        
        if 2*k+1 > len(nums):
            return ans

        sum_ = sum(nums[:k+k+1])
        ans[k] = sum_//(2*k+1)
        
        for i in range(k+1, len(nums)-k):
            sum_ = sum_- nums[i-k-1] + nums[i+k]
            
            ans[i] = sum_//(2*k+1)
        
        return ans
