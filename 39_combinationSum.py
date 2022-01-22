# 39. Combination Sum

def backtrack(candidates, target, res, arr):
    
    if target<0:
        return 
    
    if target==0:
        if arr not in res:
            res.append(arr.copy())
        return    
    
    for i in range(len(candidates)):
        arr.append(candidates[i])
        target = target-candidates[i]
        backtrack(candidates[i:], target, res, arr)
        target+=candidates[i]
        arr.pop()
    
    return

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        arr = []
        backtrack(sorted(candidates), target, res, arr)
        return res
        
