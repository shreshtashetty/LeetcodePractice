# 1184. Distance Between Bus Stops

class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        
        totalDist = 0
        clockwise_dist = 0
        
        for i in range(len(distance)):
            
            if (start<destination and i<destination and i>=start):
                clockwise_dist+=distance[i]
            
            if (start>destination and i<=start and i<destination):
                clockwise_dist+=distance[i]
                
            if (start>destination and i>=start and i<len(distance)):
                clockwise_dist+=distance[i]
                
            totalDist += distance[i]

            
        return min(totalDist-clockwise_dist, clockwise_dist)
