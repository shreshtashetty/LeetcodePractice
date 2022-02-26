# 695. Max Area of Island (Recursive)

def islandArea(grid, i, j, visited, area):
    area+=1
    
    if i-1>=0 and grid[i-1][j]==1 and (i-1,j) not in visited:
        visited.add((i-1, j))
        area = islandArea(grid, i-1, j, visited, area)
        
    if j-1>=0 and grid[i][j-1]==1 and (i,j-1) not in visited:
        visited.add((i, j-1))
        area = islandArea(grid, i, j-1, visited, area)
        
    if i+1<=len(grid)-1 and grid[i+1][j]==1 and (i+1,j) not in visited:
        visited.add((i+1, j))
        area = islandArea(grid, i+1, j, visited, area)
    
    if j+1<=len(grid[0])-1 and grid[i][j+1]==1 and (i,j+1) not in visited:
        visited.add((i, j+1))
        area = islandArea(grid, i, j+1, visited, area)
        
    return area

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) in visited:
                    continue
                else:
                    visited.add((i,j))
                    if grid[i][j]==1:
                        area = islandArea(grid, i, j, visited, 0)
                        if max_area<area:
                            max_area = area
        return max_area
    
