# 525. Contiguous Array

# Nick White's Solution: https://www.youtube.com/watch?v=nSEO5zOwP7g

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        hash_map = {}
        max_len = 0
        count = 0
        hash_map[0] = -1
        
        for i in range(len(nums)):
            if nums[i]==0:
                count-=1
            else:
                count+=1
            
            if count in hash_map:
                max_len = max(max_len, i-hash_map[count])
            else:
                hash_map[count] = i
                
        return max_len
