# 48. Rotate Image

# Transpose and flip

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if len(matrix) == 1 and len(matrix[0])==1:
            return matrix
        
        for i in range(len(matrix)):
            for j in range(i, len(matrix)):
                if i==j:
                    continue
                else:
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # print(matrix)
        
        
        for cnt in range(len(matrix)):
            i = 0
            j = len(matrix)-1
            while(i<j):
                matrix[cnt][i], matrix[cnt][j] = matrix[cnt][j], matrix[cnt][i]
                i+=1
                j-=1
