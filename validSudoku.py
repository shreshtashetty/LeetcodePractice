# 36. Valid Sudoku

# BOTH SOLUTIONS WORK AND HAVE THE SAME RUNTIME AND MEMORY USAGE
import numpy as np

# class Solution:
#     #THEIR SOLUTION
#     def isValidSudoku(self, board):
#         """
#         :type board: List[List[str]]
#         :rtype: bool
#         """
#         # init data
#         rows = [{} for i in range(9)]
#         columns = [{} for i in range(9)]
#         boxes = [{} for i in range(9)]
#         print(rows, columns, boxes)
#         # validate a board
#         for i in range(9):
#             for j in range(9):
#                 num = board[i][j]
#                 if num != '.':
#                     num = int(num)
#                     box_index = (i // 3 ) * 3 + j // 3
                    
#                     # keep the current cell value
#                     rows[i][num] = rows[i].get(num, 0) + 1
#                     columns[j][num] = columns[j].get(num, 0) + 1
#                     boxes[box_index][num] = boxes[box_index].get(num, 0) + 1
                    
#                     # check if this value has been already seen before
#                     if rows[i][num] > 1 or columns[j][num] > 1 or boxes[box_index][num] > 1:
#                         return False         
#         return True

# MY SOLUTION
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        buckets = {}
        for i in range(9):
            if i<3:
                buckets[i]=(0, 3)
            if i>=3 and i<6:
                buckets[i]=(3, 6)
            if i>=6:
                buckets[i]=(6, 9)

        board = np.array(board)
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i,j]!=".":
                    num = board[i,j]
                    if num in board[i+1:,j]:
                        return False
                    if num in board[i,j+1:]:
                        return False
                    range1, range2 = buckets[i], buckets[j]
                    window = board[range1[0]:range1[1],range2[0]:range2[1]]
                    count = 0
                    for k in range(len(window)):
                        if num in window[k,:]: 
                            count+=1
                    if count>1:
                        return False
        return True
                    
