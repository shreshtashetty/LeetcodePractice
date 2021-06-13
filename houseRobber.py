# 198. House Robber

class Solution:
    def rob(self, nums: List[int]) -> int:

        for i in range(len(nums)-3, -1, -1):
            arr = nums[i+2:]
            val = max([x+nums[i] for x in arr])
            nums[i] = val

        return max(nums)
    
