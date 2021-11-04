# 326. Power of Three

# BASIC RECURSION PROBLEM

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        
        if n==0:
            return False
        
        if n==1:
            return True
        
        return self.isPowerOfThree(n/3)
