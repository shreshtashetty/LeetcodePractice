# 695. Max Area of Island
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visitedNodes = set()  

        def findIsland(grid, i, j, visitedNodes):
            ones = []
            ones.append((i, j))
            
            k = 0
            while(k<len(ones)):
                if(ones[k][1]>=1):
                    left = (ones[k][0], ones[k][1]-1)
                    visitedNodes.add(left)
                    if(grid[ones[k][0]][ones[k][1]-1]==1 and left not in ones):
                        ones.append(left)
                    
                if(ones[k][1]<len(grid[0])-1):
                    right = (ones[k][0], ones[k][1]+1)
                    visitedNodes.add(right)
                    if(grid[ones[k][0]][ones[k][1]+1]==1 and right not in ones):
                        ones.append(right)
                    
                if(ones[k][0]>=1):
                    up = (ones[k][0]-1, ones[k][1])
                    visitedNodes.add(up)
                    if(grid[ones[k][0]-1][ones[k][1]]==1 and up not in ones):
                        ones.append(up)
                    
                if(ones[k][0]<len(grid)-1):
                    down = (ones[k][0]+1, ones[k][1])
                    visitedNodes.add(down)
                    if(grid[ones[k][0]+1][ones[k][1]]==1 and down not in ones):
                        ones.append(down)
                k+=1
            return len(ones), visitedNodes            
            
        max_area = 0
        
        for i in range(len(grid)):
            
            for j in range(len(grid[0])):
                
                if((i, j) not in visitedNodes):
                    visitedNodes.add((i, j))
                    
                    if(grid[i][j]==1):
                        area, visitedNodes = findIsland(grid, i, j, visitedNodes)
                        if(max_area<area):
                            max_area = area

        return max_area
        
