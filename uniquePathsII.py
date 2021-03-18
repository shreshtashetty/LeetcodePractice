# 63. Unique Paths II

# DP from start to finish
import numpy as np

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        obstacle_grid = np.array(obstacleGrid)
        m, n = obstacle_grid.shape
        dp = np.zeros((m, n))
        
        if obstacle_grid[0, 0] == 1 or obstacle_grid[m-1, n-1]==1:
            return 0
        
        for i in range(n): #setting row 0 elements to 1 unless obstacle  
            if obstacle_grid[0, i] ==1:
                dp[0, i] = 0
            else:
                if i==0:
                    dp[0, i] = 1
                elif i>0 and dp[0, i-1] == 1:
                    dp[0, i] = 1
                elif i>0 and dp[0, i-1]==0:
                    dp[0, i] = 0
                
        for i in range(m): #setting column 0 elements to 1 unless obstacle 
            if obstacle_grid[i, 0] ==1:
                dp[i, 0] = 0
            else:
                if i==0:
                    dp[i, 0] = 1
                elif i>0 and dp[i-1, 0]==1:
                    dp[i, 0] = 1
                elif i>0 and dp[i-1, 0]==0:
                    dp[i, 0] = 0
                
        for i in range(1, m):
            for j in range(1, n):
                if obstacle_grid[i, j] == 1:
                    pass
                else:
                    dp[i,j] = dp[i, j-1] + dp[i-1, j]

        return int(dp[m-1, n-1])
        
