# 46. Permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # MY SOLUTION
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
           
# # https://www.youtube.com/watch?v=DBLUa6ErLKw

# class Solution:
#     def __init__(self):
#         self.res = []
    
#     def backtrack(self, nums, path):
#         if not nums:
#             self.res.append(path)
#         for i in range(len(nums)):
#             self.backtrack(nums[:i]+nums[i+1:], path+[nums[i]])
#         return
        
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         self.backtrack(nums, [])
#         return self.res
