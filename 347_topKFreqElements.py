# 347. Top K Frequent Elements

# Anish Malla: https://www.youtube.com/watch?v=Vru4ooOMjX0

from collections import defaultdict
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # Using heap
        
        ans = []
        
        hash_set = defaultdict(int)
        
        for i in range(len(nums)):
            hash_set[nums[i]]+=1
        
        for key, val in hash_set.items():
            
            if len(ans)<k:
                heapq.heappush(ans, [val, key])  
            else:
                heapq.heappushpop(ans, [val,key])
                
        return [key for value, key in ans]
        
        '''
        # O(nlogn) Solution: 
        
        hash_set = defaultdict(int)
        
        for i in range(len(nums)):
            hash_set[nums[i]]+=1
            
        hash_set = dict(sorted(hash_set.items(), key=lambda x:x[1], reverse=True))
        
        res = []
        
        for key, value in hash_set.items():
            k-=1
            res.append(key)
            if k==0:
                break
                
        return res
        '''
        
        
