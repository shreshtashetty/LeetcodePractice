# 46. Permutations

# https://www.youtube.com/watch?v=DBLUa6ErLKw

class Solution:
    def __init__(self):
        self.res = []
    
    def backtrack(self, nums, path):
        if not nums:
            self.res.append(path)
        for i in range(len(nums)):
            self.backtrack(nums[:i]+nums[i+1:], path+[nums[i]])
        return
        
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.backtrack(nums, [])
        return self.res
