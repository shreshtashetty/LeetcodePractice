# 532. K-diff Pairs in an Array

# https://www.youtube.com/watch?v=r3oiTXIINOU

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:

        if k<0:
            return 0
        res = 0
        
        hash_map = {}
        
        for i in range(len(nums)):
            hash_map[nums[i]] = 1+hash_map.get(nums[i],0)
          
        for key, value in hash_map.items():
            if k==0:
                if value>1:
                    res+=1
            else:
                if key+k in hash_map:
                    res+=1
        return res
