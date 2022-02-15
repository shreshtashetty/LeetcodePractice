# 136. Single Number

# apparently, can be done in constant space complexity using bit manipulation

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashmap = {}
        
        for i in range(len(nums)):
            hashmap[nums[i]] = 1+hashmap.get(nums[i],0)
            
        for key in hashmap.keys():
            if hashmap[key]==1:
                return key
            
        return -1
                
