# 2022. Convert 1D Array Into 2D Array

class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        
        if m*n !=len(original):
            return []
        
        r = []
        k =  0
        
        for i in range(m):
            
            c = []
            
            for j in range(n):
                
                c.append(original[k])
                k+=1
                
            r.append(c)
            
        return r
