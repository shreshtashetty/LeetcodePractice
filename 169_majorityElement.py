# 169. Majority Element

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        max_elem = 0
        max_count = 0
        hash_map = {}
        
        for i in range(len(nums)):
            hash_map[nums[i]] = 1+hash_map.get(nums[i],0)
            if max_count<hash_map[nums[i]]:
                max_elem = nums[i]
                max_count = hash_map[nums[i]]
                
        return max_elem
