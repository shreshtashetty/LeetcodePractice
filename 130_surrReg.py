# 130. Surrounded Regions

def dfs(board, i, j, res):
    
    def isValid(i,j):
        
        if i>=0 and i<len(board) and j>=0 and j<len(board[i]):
            return True
        else:
            return False
        
    if isValid(i,j):
        if board[i][j]=='O' and (i,j) not in res:
            res.append((i,j))
            dfs(board, i-1, j, res)
            dfs(board, i+1, j, res)
            dfs(board, i, j-1, res)
            dfs(board, i, j+1, res)
        else:
            return
    else:
        return

    return                
        
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        Os = []
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j]=='O':
                    Os.append((i,j))
          
        res = []       
        
        for i in range(len(Os)):
            if (Os[i][0]==0 or Os[i][0]==len(board)-1) or (Os[i][1]==0 or Os[i][1]==len(board[Os[i][0]])-1):
                # res.append((Os[i][0], Os[i][1]))
                dfs(board, Os[i][0], Os[i][1], res)

        for i in range(len(Os)):
            if Os[i] not in res:
                board[Os[i][0]][Os[i][1]]='X'
        
        
            
            
