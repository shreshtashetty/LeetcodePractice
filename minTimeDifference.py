# 539. Minimum Time Difference

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        
        for i in range(len(timePoints)):
            hrs, mins = timePoints[i].split(":")
            timePoints[i] = int(hrs)*60 + int(mins)
   
        hash_map = {}
        
        for i in range(1440):
            hash_map[i] = 0
            
        for i in range(len(timePoints)):
            hash_map[timePoints[i]]+=1
            if hash_map[timePoints[i]]>1:
                return 0
            
        prev = first = -1
        min_diff = float("infinity")
     
        for i in range(1440):
            if hash_map[i]==1:
                if prev!=-1:
                    min_diff = min(i-prev, min_diff)
                else:
                    first = i
                prev = i

        min_diff = min(min_diff, 1440-prev+first)
        
        return min_diff
                
                
        
