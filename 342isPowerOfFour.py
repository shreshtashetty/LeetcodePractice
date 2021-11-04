# 342. Power of Four

class Solution:
    
    """
    # SOLUTION WITHOUT RECURSION (BIT MANIPULATION)
    # If there are even number of zeroes followed by a single 1 in binary then it is a power of 4:

    class Solution:
        def isPowerOfFour(self, n: int) -> bool:
            if(n<0):
                return False
            b = bin(n)
            if(b.count("1") == 1 and (b[3:].count("0")%2 == 0)):
                return True
            return False
    """
    def isPowerOfFour(self, n: int) -> bool:
        
        if n==0:
            return False
        
        if n==1:
            return True
        
        return self.isPowerOfFour(n/4)
        
