# 40. Combination Sum II

# https://www.youtube.com/watch?v=IER1ducXujU&list=PLi9RQVmJD2fZgRyOunLyt94uVbJL43pZ_&index=33

import copy
def solns(result, current, ind, candidates, target):
    
    if target==0:
        # print(current)
        result.append(copy.deepcopy(current))
        return
    
    if target<0:
        return
    
    for i in range(ind, len(candidates)):
        if i==ind or candidates[i]!=candidates[i-1]:
            
            current.append(candidates[i])
            solns(result, current, i+1, candidates, target-candidates[i])
            current.pop()    
            
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        # print(candidates)
        result = []
        current = []
        solns(result, current, 0, candidates, target)
        return result
        
