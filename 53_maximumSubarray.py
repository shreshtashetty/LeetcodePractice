#53. Maximum Subarray

# Kadane's Algorithm
# Nick White's explanation: https://www.youtube.com/watch?v=jnoVtCKECmQ

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        curr = nums[0]
        max_sum = nums[0]
        
        for x in nums[1:]:
            curr = max(curr+x, x)
            max_sum = max(curr, max_sum)
        return max_sum
        
        # MY HACKY SOLUTION
        # for x in nums[1:]:
        #     if curr+x>x and curr+x>curr:
        #         curr+=x
        #     else:
        #         if curr>max_sum:
        #             max_sum = curr
        #         curr = max(curr+x, x)
        # return max(curr, max_sum)
                

# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         if len(nums) == 1:
#             return sum(nums)
        
#         Sums = []
#         curr = nums[0]
#         for x in nums[1:]:
#             if (curr+x > x) and (curr+x > curr):
#                 curr+=x
#             else:
#                 Sums.append(curr)
#                 curr = max(curr+x, x)
                
#         Sums.append(curr)
#         return max(Sums)
    
#         if(len(nums)==1):
#             return nums[0]
        
#         m = max(nums)
#         s = 0
#         for i in range(len(nums)):
#             s+=nums[i]
#             nums[i] = s   
            
#         if(m<max(nums)):
#             m = max(nums)
        
#         import numpy as np
#         nums = np.array(nums)
        
#         for i in range(len(nums)-2):
#             nums[i:] = nums[i:]-nums[i] 
#             if(max(nums[i+1:])>m):
#                 m = max(nums)
#         return m
