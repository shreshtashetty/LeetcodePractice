# 2150. Find All Lonely Numbers in the Array

class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        
        nums_unique = set(nums)
        hash_map = {}
        
        for n in nums:
            hash_map[n] = hash_map.get(n,0)+1
        
        lonely_nums = []
        
        for i in range(len(nums)):
            if nums[i]-1 not in nums_unique and nums[i]+1 not in nums_unique and hash_map[nums[i]]==1:
                lonely_nums.append(nums[i])
                
        return lonely_nums
