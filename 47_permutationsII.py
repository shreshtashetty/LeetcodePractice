# 47. Permutations II

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        l = len(nums)
        
        def givePermute(nums, res, arr):
    
            if len(arr)==l and arr not in res:
                res.append(arr.copy())
                return 

            for i in range(len(nums)):
                arr.append(nums[i])
                givePermute(nums[:i]+nums[i+1:], res, arr)
                arr.pop()

            return
        
        givePermute(nums, res, [])
        return res
