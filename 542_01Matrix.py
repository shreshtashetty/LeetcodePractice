# 542. 01 Matrix

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        ROWS, COLUMNS = len(mat), len(mat[0])
        grid = [[0 for _ in range(COLUMNS)] for _ in range(ROWS)] 
        queue = deque()
        visited = [[False for _ in range(COLUMNS)] for _ in range(ROWS)]
        
        for row in range(ROWS):
            for column in range(COLUMNS):
                if mat[row][column] == 0: 
                    queue.append((row, column, 0))
                    visited[row][column] = True
           
        while queue:
            
            row, column, distance = queue.popleft()
            for x, y in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                r, c = row + x, column + y
                if r in range(ROWS) and c in range(COLUMNS) and not visited[r][c]:
                    grid[r][c] = distance+1
                    queue.append((r, c, distance+1))
                    visited[r][c] = True
                    
        return grid
