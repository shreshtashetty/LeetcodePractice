# 268. Missing Number

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums_sort = sorted(nums)
        
        if nums_sort[-1]<len(nums):
            return len(nums)
        
        if nums_sort[0]!=0:
            return 0
        
        for i in range(len(nums)-1):
            if nums_sort[i+1]-nums_sort[i]!=1:
                return nums_sort[i]+1
        
        
            
        
