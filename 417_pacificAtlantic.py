# 417. Pacific Atlantic Water Flow

'''
class Solution:
    # MY SOLUTION. CORRECT BUT EXCEEDS TIME LIMIT. O(M.N)**2
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        def findOceans(cell, arr, seen):
            seen.add(cell)
            if (cell[0] == 0 and cell[1] == len(heights[0])-1) or (cell[0] == len(heights)-1 and cell[1] == 0):
 
                return [True,True]
            
            if cell[0]==0 or cell[1]==0:
                arr[0] = True

            if cell[0]==len(heights)-1 or cell[1]==len(heights[0])-1:
                arr[1] = True
            
            if arr[0] and arr[1]:
                return arr

            arr = arr.copy()
            res = []
            
            if cell[0]<len(heights)-1 and heights[cell[0]+1][cell[1]]<=heights[cell[0]][cell[1]] and (cell[0]+1,cell[1]) not in seen:
                south = findOceans((cell[0]+1, cell[1]), arr, seen)
                res.append(south)
                
            if cell[1]<len(heights[0])-1 and heights[cell[0]][cell[1]+1]<=heights[cell[0]][cell[1]] and (cell[0],cell[1]+1) not in seen:
                east = findOceans((cell[0], cell[1]+1), arr, seen)
                res.append(east)
                
            if cell[0]>0 and heights[cell[0]-1][cell[1]]<=heights[cell[0]][cell[1]] and (cell[0]-1,cell[1]) not in seen:
                north = findOceans((cell[0]-1, cell[1]), arr, seen)
                res.append(north)
                
            if cell[1]>0 and heights[cell[0]][cell[1]-1]<=heights[cell[0]][cell[1]] and (cell[0],cell[1]-1) not in seen:
                west = findOceans((cell[0], cell[1]-1), arr, seen)
                res.append(west)
                
            # print(cell, res)
            for i in res:
                if i[0]:
                    arr[0] = True
                if i[1]:
                    arr[1] = True
            
            return arr

        res = []
        
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                seen = set()
                vals = findOceans((i,j), [False, False], seen)
                if vals[0] and vals[1]:
                    res.append([i,j])

        return res
'''
# SOLUTION MORE OR LESS SIMILAR TO THE ONE IN: https://www.youtube.com/watch?v=s-VkcjHqkGI
# # O(M*N)

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
    
        nRows = len(heights)
        nCols = len(heights[0])
        
        lRow = nRows-1
        lCol = nCols-1
        
        reachPacific = []
        reachAtlantic = []
        for i in range(nRows):
            reachPacific.append([False]*nCols)
            reachAtlantic.append([False]*nCols)
        
        def dfs(reachOcean, i, j, prevH = 0):
            # check i and j
            if i>lRow or j>lCol or i<0 or j<0:
                return
            
            # if already know ocean can be reached from here
            if reachOcean[i][j]:
                return
            
            # check if ocean can be reached from here
            h = heights[i][j]
            if h<prevH:
                return
            reachOcean[i][j] = True
            
            # move to adjacent squares
            dfs(reachOcean, i+1, j, h)
            dfs(reachOcean, i-1, j, h)
            dfs(reachOcean, i, j+1, h)
            dfs(reachOcean, i, j-1, h)
        
        # try to reach each square on
        # pacific left coast
        for i in range(nRows):
            dfs(reachPacific, i, 0)
        
        # try to reach each square on
        # pacific top coast
        for j in range(nCols):
            dfs(reachPacific, 0, j)

        # try to reach each square on
        # atlantic right coast
        for i in range(nRows):
            dfs(reachAtlantic, i, lCol)
        
        # try to reach each square on
        # atlantic bottom coast
        for j in range(nCols):
            dfs(reachAtlantic, lRow, j)
            
        res = []
        for i in range(nRows):
            for j in range(nCols):
                if reachAtlantic[i][j] and reachPacific[i][j]:
                    res.append([i,j])
        return res
