# 136. Single Number

# apparently, can be done in constant space complexity using bit manipulation

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        occ = {}
        
        for i in range(len(nums)):
            if nums[i] not in occ:
                occ[nums[i]] = 1
            else:
                occ[nums[i]] += 1
                
        for i in range(len(nums)):
            if occ[nums[i]]==1:
                return nums[i]
                
