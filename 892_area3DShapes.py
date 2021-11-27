# 892. Surface Area of 3D Shapes

def valid_indices(i, j, grid):
    inds = []
    if i>0:
        inds.append((i-1, j))
    if  j>0:
        inds.append((i, j-1))
    if i<len(grid)-1:
        inds.append((i+1, j))
    if j<len(grid[i])-1:
        inds.append((i, j+1))
    return inds
    
    
class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        total = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]==0:
                    continue
                else:
                    init_area = 4*(grid[i][j]) + 2
                inds = valid_indices(i, j, grid)
                for k in inds:
                    if grid[k[0]][k[1]]<grid[i][j]:
                        init_area-=grid[k[0]][k[1]]
                    else:
                        init_area-=grid[i][j]
                total+=init_area
                
        return total
