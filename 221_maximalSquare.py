# 221. Maximal Square

# Refer to their Dynamic Programming Solution

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        import numpy as np
      
        if len(matrix)==1 and len(matrix[0])==1:
                return 0 if matrix[0][0]=="0" else 1
        
        dp = np.zeros((len(matrix), len(matrix[0])))
        
        maxSeqLen = 0
        
        for i in range(len(dp)):
            if matrix[i][0]=="1":
                dp[i][0]=1
                maxSeqLen = 1
                
        for i in range(1,len(dp[0])):
            if matrix[0][i]=="1":
                dp[0][i]=1
                maxSeqLen = 1
    
        if (len(matrix)==1 and len(matrix[0])>1) or (len(matrix[0])==1 and len(matrix)>1):
            return maxSeqLen
        
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if matrix[i][j]=="1":
                    dp[i][j] = 1+min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1])
                    if dp[i][j]>maxSeqLen:
                        maxSeqLen = dp[i][j]
                        
        return int(maxSeqLen**2)
            
        
        
        
        
