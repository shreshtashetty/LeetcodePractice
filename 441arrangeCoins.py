# 441. Arranging Coins

class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        # BINARY SEARCH SOLUTION
        left, right = 0, n
        
        while left <= right:
            
            k = (right + left) // 2
            curr = k * (k + 1) // 2
            
            if curr == n:
                return k
            
            if n < curr:
                right = k - 1
                
            else:
                left = k + 1
                
        return right
        
#         # MATH SOLUTION
#         return int(((2*n+0.25)**0.5)-0.5)
    
#         # ITERATIVE SOLUTION
#         i = 1
#         count = 0
        
#         while(n>=0):
            
#             n = n-i
#             i+=1
#             if n>=0:
#                 count+=1
            
#         return count
            
            
        
