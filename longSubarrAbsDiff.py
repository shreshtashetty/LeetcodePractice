# 1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit

from collections import deque

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
    
        i=0
        ans=0
        max_d = deque([])#decreasing order deque
        min_d = deque([])#increasing order deque
        
        for j in range(len(nums)):
            
            while min_d and nums[j]<nums[min_d[-1]]:
                min_d.pop()
            min_d.append(j)
            
            while max_d and nums[j]>nums[max_d[-1]]:
                max_d.pop()
            max_d.append(j)

            if nums[max_d[0]]-nums[min_d[0]]<=limit:
                ans = max(j-i+1, ans)
            else:
                if nums[max_d[0]]==nums[i]:
                    max_d.popleft()
                if nums[min_d[0]]==nums[i]:
                    min_d.popleft()
                i+=1
        return ans
        
        
            
