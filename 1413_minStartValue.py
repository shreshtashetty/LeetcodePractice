# 1413. Minimum Value to Get Positive Step by Step Sum

class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        
        most_negative = 0
        
        start = 0
        
        for i in range(len(nums)):
            step_sum = start + nums[i]
            if step_sum<most_negative:
                most_negative = step_sum
            start = step_sum
        
        if most_negative==0:
            return 1
        else:
            return 1+(-most_negative)
