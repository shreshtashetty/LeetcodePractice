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
            x_sqrt = x//mid
            
            if mid==x_sqrt:
                return mid
            
            if mid<x_sqrt:
                l = mid+1 
            else:
                r = mid-1
                ans = x_sqrt # floor value used in case number has no integer square root.
                
        return ans
