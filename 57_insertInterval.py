# 57. Insert Interval

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        intervals.append(newInterval)
        
        if len(intervals)<1:
            return intervals
        
        intervals = sorted(intervals)
        
        curr_interval = intervals[0]
        output_intervals = [curr_interval]
        
        for i in range(len(intervals)):
            
            curr_begin = curr_interval[0]
            curr_end = curr_interval[1]
            
            next_begin = intervals[i][0]
            next_end = intervals[i][1]
            
            if curr_end>=next_begin:
                curr_interval[1] = max(curr_end, next_end)
            else:
                curr_interval = intervals[i]
                output_intervals.append(curr_interval)
                
                
        return output_intervals
