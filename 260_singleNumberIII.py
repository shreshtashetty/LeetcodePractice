# 260. Single Number III

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        
        hash_map = {}
        
        for i in nums:
            if i not in hash_map:
                hash_map[i]=1
            else:
                hash_map[i]+=1

        result = []   
        
        for k, v in hash_map.items():
            if v==1:
                result.append(k)
        return result
        
