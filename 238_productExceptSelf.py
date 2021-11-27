# 238. Product of Array Except Self

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        if 0 in nums:
            res = [0]*len(nums)
            if nums.count(0)>1:
                return res
            product = 1
            ind = 0
            for i in range(len(nums)):
                if nums[i]!=0:
                    product*=nums[i]
                else:
                    ind = i
            res[ind]=product
            return res
        
        # O(n) solution  without using division operation
        l = [0]*len(nums)
        l[0] = 1
        r = [0]*len(nums)
        r[-1] = 1
        
        for i in range(1, len(nums)):
            l[i] = l[i-1]*nums[i-1]
        
        for i in range(len(nums)-2, -1, -1):
            r[i] = r[i+1]*nums[i+1]
            
        for i in range(len(nums)):
            l[i] = l[i]*r[i]
            
        return l
        
            
                
