# 289. Game of Life

from collections import Counter

class Solution:
        
    
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def isValidNeighbor(i, j):
            if i>=0 and i<len(board) and j>=0 and j<len(board[0]):
                return 1
            else:
                return 0
        
        def getneighbors(i, j):

            neighbs = []
            if isValidNeighbor(i-1, j-1):
                neighbs.append(board[i-1][j-1])
            if isValidNeighbor(i, j-1):
                neighbs.append(board[i][j-1])
            if isValidNeighbor(i+1, j-1):
                neighbs.append(board[i+1][j-1])
            if isValidNeighbor(i-1, j):
                neighbs.append(board[i-1][j])
                
            if isValidNeighbor(i-1, j+1):
                neighbs.append(board[i-1][j+1])
            if isValidNeighbor(i, j+1):
                neighbs.append(board[i][j+1])
            if isValidNeighbor(i+1, j+1):
                neighbs.append(board[i+1][j+1])
            if isValidNeighbor(i+1, j):
                neighbs.append(board[i+1][j])

            return neighbs
        
        d = {}
        m = len(board)
        n = len(board[0])
        
        if len(board)==1 and len(board[0])==1:
            board[0][0] = 0
            return board
        
        for i in range(m):
            for j in range(n):
                d[(i, j)] = [board[i][j], Counter(getneighbors(i, j))]
                
        for keys, values in d.items():
            val, neighbs = values
            # print(keys, val, neighbs[1])
            
            if val == 1 and neighbs[1]<2:
                board[keys[0]][keys[1]]=0
                
            if val == 1 and neighbs[1]==2 or neighbs[1]==3:
                pass
            
            if val == 1 and neighbs[1]>3:
                board[keys[0]][keys[1]]=0
                
            if val == 0 and neighbs[1]==3:
                board[keys[0]][keys[1]]=1
                
        return board
            
