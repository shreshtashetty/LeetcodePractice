# 775. Global and Local Inversions

class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        
        min_elem = nums[-1]
        
        for i in range(len(nums)-3, -1, -1):
            
            if nums[i]>min_elem:
                return False
            
            min_elem = min(min_elem, nums[i+1])
            
        return True
