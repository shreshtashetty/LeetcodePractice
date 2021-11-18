# 448. Find All Numbers Disappeared in an Array

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        hash_map = {}
        
        n = len(nums)
        
        for i in range(n):
            hash_map[i+1] = 0
            
        for i in range(len(nums)):
            hash_map[nums[i]]+=1
            
        res = []
        
        for key, value in hash_map.items():
            if value == 0:
                res.append(key)
                
        return res
