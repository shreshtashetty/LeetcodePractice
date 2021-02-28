#73. Set Matrix Zeroes
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = []
        cols = []
        for i in range(len(matrix)):
            if(0 in matrix[i]):
                ind = [j for j, x in enumerate(matrix[i]) if x == 0]
                if(i not in rows):
                    rows.append(i)
                for j in ind:
                    if j not in cols:
                        cols.append(j)
        
        for i in rows:
            for j in range(len(matrix[i])):
                matrix[i][j]=0
        
        for i in cols:
            for j in range(len(matrix)):
                matrix[j][i]=0
        
