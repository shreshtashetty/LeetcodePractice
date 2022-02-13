# 560. Subarray Sum Equals K

# Neetcode's explanation: https://www.youtube.com/watch?v=fFVZt-6sgyo

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        ans = 0
        prefsum = 0
        d = {0:1}
        
        for num in nums:
            prefsum = prefsum + num
            
            if prefsum-k in d:
                ans = ans + d[prefsum-k]
            
            if prefsum not in d:
                d[prefsum] = 1
            else:
                d[prefsum] = d[prefsum]+1
        
        return ans
        
#         cnt = 0
        
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)+1):
#                 if sum(nums[i:j])==k:
#                     cnt+=1
                    
#         return cnt
