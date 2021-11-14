# 59. Spiral Matrix II

# For a basic explanation, refer to Nick White's video: https://www.youtube.com/watch?v=NO1zLdOwgR0

import numpy as np

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        mat = np.zeros((n,n), dtype=np.int32)
    
        i, j = 0, 0
        num = 1
        
        rowBeg, colBeg = 0, 0
        rowEnd, colEnd = n-1, n-1
        
        while(rowBeg<=rowEnd and colBeg<=colEnd):
            
            for i in range(colBeg, colEnd+1):
                mat[rowBeg,i] = num
                num+=1
                
            rowBeg+=1
            
            for i in range(rowBeg, rowEnd+1):
                mat[i,colEnd] = num
                num+=1
                
            colEnd-=1
            
            for i in range(colEnd, colBeg-1, -1):
                mat[rowEnd,i] = num
                num+=1
                
            rowEnd-=1
            
            for i in range(rowEnd, rowBeg-1, -1):
                mat[i,colBeg] = num
                num+=1
                
            colBeg+=1
            
        return mat
            
        
        
