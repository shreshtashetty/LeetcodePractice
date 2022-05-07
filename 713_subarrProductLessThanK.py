# 713. Subarray Product Less Than K

# Crux: count += p2 - p1 + 1. number of subarrays in an interval the product of whose elements <k
# is the same as the length of the interval.

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        
        if k<=1:
            return 0
        
        p1, p2 = 0, 0
        count = 0
        prod = 1
        
        while p2<len(nums) and p1<=p2:
            
            prod *= nums[p2]
            
            while prod>=k:
                prod//=nums[p1]
                p1+=1
            
            count += p2-p1+1
            
            p2+=1
        
                
        return count
            
