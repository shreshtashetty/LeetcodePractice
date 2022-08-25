# 807. Max Increase to Keep City Skyline

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        
        max_r = []
        max_c = []
        
        for i in range(len(grid)):
            max_r.append(max(grid[i]))
            
        grid_t = list(zip(*grid))
        r, c = len(grid), len(grid_t)
        
        for j in range(c):
            max_c.append(max(grid_t[j]))
        
        max_increase = 0
        for i in range(r):
            for j in range(c):
                height = min(max_r[i], max_c[j])
                max_increase += (height-grid[i][j])
                
        return max_increase
        
            
