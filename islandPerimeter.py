# 463. Island Perimeter

def perimeterCalc(perimeter, grid, i, j, visited):
    
    if (i,j) in visited:
        return perimeter
    else:
        visited.add((i,j))
    
    if grid[i][j]==1:
        
        if i==0:
            perimeter+=1

        if j==0:
            perimeter+=1

        if i==len(grid)-1:
            perimeter+=1

        if j==len(grid[0])-1:
            perimeter+=1

        if i-1>=0 and grid[i-1][j]==0:
            perimeter+=1

        if i+1<=len(grid)-1 and grid[i+1][j]==0:
            perimeter+=1

        if j-1>=0 and grid[i][j-1]==0:
            perimeter+=1

        if j+1<=len(grid[0])-1 and grid[i][j+1]==0:
            perimeter+=1
            
    
    if i-1>=0:
        perimeter = perimeterCalc(perimeter, grid, i-1, j, visited)
        
    if i+1<=len(grid)-1:
        perimeter = perimeterCalc(perimeter, grid, i+1, j, visited)
        
    if j-1>=0:
        perimeter = perimeterCalc(perimeter, grid, i, j-1, visited)
        
    if j+1<=len(grid[0])-1:
        perimeter = perimeterCalc(perimeter, grid, i, j+1, visited)
        
    return perimeter

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        perimeter = 0
        visited = set()
        perimeter = perimeterCalc(perimeter, grid, 0, 0, visited)

        return perimeter
        
                   
            
                
        
