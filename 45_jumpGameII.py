# 45. Jump Game II

# https://www.youtube.com/watch?v=dJ7sWiOoK7g

from collections import deque

class Solution:
    def jump(self, nums: List[int]) -> int:
        
        res = 0   
        l = r = 0
                
        while r<len(nums)-1:
            
            farthest = 0
            
            for i in range(l, r+1):
                farthest = max(farthest, i+nums[i])
                
            l = r+1
            r = farthest
            res+=1
        
        return res
                
                
#         MY SOLUTION THAT IS CORRECT BUT EXCEEDS TIME LIMIT                
        
#         n = 0
#         group = deque([0])
#         prev = []
        
#         while(len(nums)-1 not in group):
            
#             for i in range(len(group)):
                
#                 ind = group.popleft()
#                 prev.append(ind)
#                 step = nums[ind]
                
                
#                 while step>0:
#                     if ind+step<len(nums) and ind+step not in group and ind+step not in prev:
#                         group.append(ind+step)
#                     step-=1
                       
#             n+=1
            
#         return n
