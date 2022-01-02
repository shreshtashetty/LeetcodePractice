# 128. Longest Consecutive Sequence

from collections import defaultdict

'''
[0,3,7,2,5,8,4,6,0,1]
[0,1,1,2]
[100,4,200,1,3,2]
[0,-1]
'''

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if len(nums)==1:
            return 1
        
        if len(nums)==0:
            return 0
        
        nums = sorted(nums)
        
        hashmap = defaultdict(int)
        ind = 0
        
        for i in range(1,len(nums)):
            
            if nums[i-1]==nums[i]:
                continue
         
            if nums[i-1]+1!=nums[i]:
                ind = i
                hashmap[nums[ind]]+=1
            else:
                if not hashmap:
                    hashmap[nums[ind]]+=1
                hashmap[nums[ind]]+=1
        
        if not hashmap:
            hashmap[nums[0]]=1
            
        maxval = -1
        
        for key,value in hashmap.items():
            
            if maxval<value:
                maxval = value
                
        return maxval
