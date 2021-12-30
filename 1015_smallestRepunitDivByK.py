# 1015. Smallest Integer Divisible by K

class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        
        if k%2==0 or k%5==0:
            return -1
        
        l = 1
        rem = 1%k
        
        seen = set()
        
        while rem!=0:
            if rem in seen:
                return -1
            else:
                seen.add(rem)
                n = rem*10 + 1
                l+=1
                rem = n%k
                
        return l
