# 1288. Remove Covered Intervals

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        
        if len(intervals)<2:
            return len(intervals)
        
        intervals = sorted(intervals)
        
        p1,p2=0,1
        
        while p2<len(intervals):
            
            if intervals[p2][0]<=intervals[p1][1] and intervals[p2][1]<=intervals[p1][1]:
                intervals.pop(p2)
                continue
                
            elif intervals[p1][0]==intervals[p2][0] and intervals[p1][1]<=intervals[p2][1]:
                intervals.pop(p1)
                continue
                
            p1+=1
            p2+=1
         
        return len(intervals)
