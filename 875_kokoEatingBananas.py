# 875. Koko Eating Bananas

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        lo = 1
        hi = max(piles)
        
        while lo<=hi:
            mid = lo+(hi-lo)//2
            hrs = sum([math.ceil(i/mid) for i in piles])
            
            # Can't do this here because we are finding the minimum value for mid, not just any value for mid. The below code might break out for a higher value of mid.
            # if hrs==h:
            #     print(lo,hi)
            #     return mid
            
            if hrs<=h: #account for the hrs==h condition here.
                hi = mid-1
            elif hrs>h:
                lo = mid+1

        return lo
