# 581. Shortest Unsorted Continuous Subarray

# Nick White's video and Leetcode's solution.

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        
        sorted_nums = sorted(nums)
        
        
        for i in range(len(nums)):
            if nums[i]!=sorted_nums[i]:
                break
                
        for j in range(len(nums)-1, -1, -1):
            if nums[j]!=sorted_nums[j]:
                break
                
        return j-i+1 if i<j else 0
