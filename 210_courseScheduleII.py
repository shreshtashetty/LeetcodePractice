# 210. Course Schedule II

# https://www.youtube.com/watch?v=VmHC5j_i2qE

from collections import defaultdict, deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = [0]*numCourses # number of edges pointing to a node
        
        # Creating the graph
        for pre, final in prerequisites:
            graph[final].append(pre)
            indegree[pre]+=1
        
        q = deque([x for x in range(numCourses) if indegree[x]==0])
        
        topological_sorted_order = []
        
        while len(q)!=0:
            node = q.popleft()
            topological_sorted_order.append(node)
            for neighbor in graph[node]:
                indegree[neighbor]-=1
                if indegree[neighbor]==0:
                    q.append(neighbor)
                    
        return topological_sorted_order if len(topological_sorted_order)==numCourses else []
        
