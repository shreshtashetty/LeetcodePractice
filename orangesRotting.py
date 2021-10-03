# 994. Rotting Oranges

from collections import deque

def toExplore(all_dirs, to_explore, visited, grid):
    for i in range(len(all_dirs)):
        if all_dirs[i] not in visited:
            r, c = all_dirs[i]
            if r>=0 and r<len(grid) and c>=0 and c<len(grid[0]):
                visited.add(all_dirs[i])
                if grid[r][c]==1:
                    to_explore.append(all_dirs[i])
    return

def fourDirections(i, j, m, n):
    dirs = []
    if i==0 and j==0:
        dirs+=[(i+1, j), (i, j+1)]
    elif i==0 and j>0 and j<n-1:
        dirs+=[(i+1, j), (i, j+1), (i, j-1)]
    elif i==0 and j==n-1:
        dirs+=[(i+1, j), (i, j-1)]
    elif j==0 and i>0 and i<m-1:
        dirs+=[(i-1, j), (i+1, j), (i, j+1)]
    elif j==0 and i==m-1:
        dirs+=[(i-1, j), (i, j+1)]
    elif i==m-1 and j>0 and j<n-1:
        dirs+=[(i, j-1), (i-1, j), (i, j+1)]
    elif i==m-1 and j==n-1:
        dirs+=[(i, j-1), (i-1, j)]
    elif j==n-1 and i>0 and i<m-1:
        dirs+=[(i-1, j), (i, j-1), (i+1, j)]
    else:
        dirs+=[(i, j-1), (i-1, j), (i, j+1), (i+1, j)]
    return dirs

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        
        if m==1 and n==1:
            if grid[0][0]==0 or grid[0][0]==2:
                return 0
            elif grid[0][0]==1:
                return -1
        queue = deque([])
        
        visited = set()
        
        all_zeros = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==2:
                    queue.append((i,j))
                    visited.add((i,j))
                if grid[i][j]==1 or grid[i][j]==2:
                    all_zeros = 1
        if all_zeros == 0:
            return 0
                
        count = -1
        
        while queue:
     
            count+=1
            to_explore = deque([])
            
            while queue:
                node = queue.popleft()
                all_dirs = fourDirections(node[0], node[1], m, n)
                toExplore(all_dirs, to_explore, visited, grid)
            queue+=to_explore
            
            for k in range(len(queue)):
                i = to_explore[k][0]
                j = to_explore[k][1]
                grid[i][j]=2

        detect_ones = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    detect_ones = 1

        if detect_ones == 1:
            return -1
        else:
            return count
