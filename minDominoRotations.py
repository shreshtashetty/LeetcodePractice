# 1007. Minimum Domino Rotations For Equal Row

def numSwaps(A0, A, B):
    swaps = 0
    for i in range(len(A)):
        if A[i]!=A0:
            if B[i]!=A0:
                swaps = -1
                break
            else:
                swaps+=1
                    
    return swaps
    
class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        import numpy as np
        
        min_swaps = np.inf
        
        swaps1 = numSwaps(A[0], A, B)
        swaps2 = numSwaps(B[0], B, A)
        swaps3 = numSwaps(A[0], B, A)
        swaps4 = numSwaps(B[0], A, B)
        
        if swaps1 == -1 and  swaps2 == -1 and swaps3 == -1 and swaps4 == -1:
            return -1
        else:
            if swaps1!=-1:
                min_swaps = min(min_swaps, swaps1)
            if swaps2!=-1:
                min_swaps = min(min_swaps, swaps2)
            if swaps3!=-1:
                min_swaps = min(min_swaps, swaps3)
            if swaps4!=-1:
                min_swaps = min(min_swaps, swaps4)
                
        return min_swaps
        
        
