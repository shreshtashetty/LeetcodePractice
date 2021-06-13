# 973. K Closest Points to Origin

from heapq import *

def sqEuclidDist(x, y):
    d_sq = x**2 + y**2
    return d_sq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        point_dists = []
        for i in range(len(points)):
            sq_dist = sqEuclidDist(points[i][0], points[i][1])
            heappush(point_dists, (sq_dist, i))
        
        closest_points = []
        for i in range(k):
            ind = heappop(point_dists)[1]
            closest_points.append(points[ind])
        return closest_points
    
        
