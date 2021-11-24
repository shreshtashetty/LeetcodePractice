# 78. Subsets

# Kevin Naughton Jr.'s solution: https://www.youtube.com/watch?v=LdtQAYdYLcE

from copy import deepcopy

def backtrack(nums, current, subsets):
    subsets.append(deepcopy(current))
    
    for i in range(len(nums)):
        current.append(nums[i])
        backtrack(nums[i+1:], current, subsets)
        current.pop()
    
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        backtrack(nums, [], subsets)
        return subsets
