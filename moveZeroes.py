# 283. Move Zeroes

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-1):
            for j in range(1, len(nums)):
                if nums[j-1] == 0:
                    nums[j-1], nums[j] = nums[j], nums[j-1]
        
