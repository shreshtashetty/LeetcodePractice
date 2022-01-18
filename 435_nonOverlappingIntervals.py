# 435. Non-overlapping Intervals

'''
[[1, 2], [1, 3], [2, 3], [2, 6], [3, 5]]
[[1, 2], [1, 3], [2, 3], [3, 4], [3, 5]]
[[1, 2], [1, 3], [3, 4], [3, 5]]
[[0, 2], [1, 3], [2, 4], [3, 5], [4, 6]]
'''

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        ints = sorted(intervals)
        
        i = 0
        j = 1
        count = 0
        del_arr = []
        
        while i <len(ints)-1 and j<len(ints):
          
            if ints[i][1]>ints[j][0]:
                count+=1
                if ints[i][1]>=ints[j][1]:
                    i = j
            elif ints[i][1]<=ints[j][0]:
                i = j
            j+=1

        return count
            
                
                
                
