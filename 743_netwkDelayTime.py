# 743. Network Delay Time

# Dijkstra's Algorithm.
# https://www.youtube.com/watch?v=EaphyqKU4PQ

import heapq
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        edges = defaultdict(list)
        
        for u, v, w in times:
            edges[u].append((v, w))
        
        minHeap = [(0,k)]
        visited = set()
        t = 0
        
        while minHeap:
            w1,n1 = heapq.heappop(minHeap)
            if n1 in visited:
                continue
            visited.add(n1)
            t = max(t, w1)
            
            for n2,w2 in edges[n1]:
                if n2 not in visited:
                    heapq.heappush(minHeap, (w1+w2, n2))
                    
        return t if len(visited)==n else -1
        
