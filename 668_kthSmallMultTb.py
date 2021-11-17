# 668. Kth Smallest Number in Multiplication Table

class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        
        # THEIR SOLUTION USING BINARY SEARCH
        
        def enough(x):
            count = 0
            for i in range(1, m+1):
                count += min(x // i, n)
            return count >= k

        lo, hi = 1, m * n
        
        while lo < hi:
            mi = (lo + hi) / 2
            if not enough(mi):
                lo = mi + 1
            else:
                hi = mi
        return int(lo)

    
#         MY BRUTE FORCE SOLUTION

#         l = []
        
#         for i in range(1, m+1):
#             for j in range(1, n+1):
#                 l.append(i*j)
        
#         l = sorted(l)
#         # print(l)
        
#         return l[k-1]
        
