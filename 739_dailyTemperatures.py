# 739. Daily Temperatures

# from collections import deque

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        # MONOTONIC STACK METHOD
        
        # For explanation look at https://www.youtube.com/watch?v=cTBiBSnjO3c
        
        n = len(temperatures)
        answer = [0] * n
        stack = []
        
        for curr_day, curr_temp in enumerate(temperatures):
            
            # Pop until the current day's temperature is not
            # warmer than the temperature at the top of the stack
            
            while stack and temperatures[stack[-1]] < curr_temp:
                
                prev_day = stack.pop()
                answer[prev_day] = curr_day - prev_day
                
            stack.append(curr_day)
        
        return answer
        
        
        
        
        
        
        
        
        
        
        
        
#         # BRUTE FORCE
#         res = deque()
        
#         for i in range(len(temperatures)-1, -1, -1):
            
#             if i==len(temperatures)-1:
#                 res.appendleft(0)
                
#             else:
#                 j = i+1
                
#                 while j<=len(temperatures)-1:
                    
#                     if temperatures[j]>temperatures[i]:
#                         break
#                     j+=1
                    
#                 if j==len(temperatures):
#                     res.appendleft(0)
                    
#                 else:
#                     res.appendleft(j-i)
                    
#         return res
            
