# 200. Number of Islands

def detectIsland(grid, i, j, visited):
    
    visited.add((i, j))
    
    if i>0 and grid[i-1][j] == "1" and (i-1, j) not in visited:
        visited = detectIsland(grid, i-1, j, visited)
    
    if i<len(grid)-1 and grid[i+1][j] == "1" and (i+1, j) not in visited:
        visited = detectIsland(grid, i+1, j, visited)
    
    if j>0 and grid[i][j-1] == "1" and (i, j-1) not in visited:
        visited = detectIsland(grid, i, j-1, visited)
    
    if j<len(grid[0])-1 and grid[i][j+1] == "1" and (i, j+1) not in visited:
        visited = detectIsland(grid, i, j+1, visited)
    
    return visited
        

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        visited = set()
        num_islands = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
   
                if (i, j) not in visited and grid[i][j]=="1":
                    num_islands+=1
                    visited = detectIsland(grid, i, j, visited)
                    
        return num_islands
                    
        
