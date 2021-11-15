# 300. Longest Increasing Subsequence

# https://www.youtube.com/watch?v=cjWnW0hdF1Y

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        lis = [1]*len(nums)
        
        for i in range(len(nums)-2, -1, -1):
            num=1
            for j in range(i+1, len(nums)):
              
                if nums[i]<nums[j]:
                    num = max(num, 1+lis[j])
            lis[i] = num
        
        return max(lis)
            
