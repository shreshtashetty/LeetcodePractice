# 69. Sqrt(x)

class Solution:
    def mySqrt(self, x: int) -> int:
        
        if x==0 or x==1:
            return x
        
        l = 0
        r = x
        ans = 0
        
        while(l<=r):
            
            mid = l + (r-l)//2
            mid_sq = mid*mid
            
            if mid_sq==x:
                return mid
            
            if mid_sq<x:
                l = mid+1
                ans = mid # floor value used in case number has no integer square root. 
            else:
                r = mid-1
                
        return ans
