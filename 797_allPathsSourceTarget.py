# 797. All Paths From Source to Target

from copy import deepcopy

def backtrack(graph, paths, l, path=[0], ind=0):
    
    if ind==l:
        if path not in paths:
            paths.append(deepcopy(path))
        else:
            path = [0]
        return
    
    for i in range(len(graph[ind])):
        path.append(graph[ind][i])
        backtrack(graph, paths, l, path, graph[ind][i])
        path.pop()
        

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        paths = []
        l = len(graph)-1
        backtrack(graph, paths, l)
        return paths
        
