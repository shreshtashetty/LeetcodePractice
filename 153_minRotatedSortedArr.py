# 153. Find Minimum in Rotated Sorted Array

class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        left, right = 0, len(nums) - 1
        
        while nums[left] > nums[right]:
            
            middle  = (left + right) // 2
            
            if nums[middle] < nums[right]:
                right = middle
            else:
                left = middle + 1
                
        return nums[left]
        
#         # MY SOLUTION: WHICH IS JUST AS FAST BUT NOT SO CLEAN

#         lo = 0
#         hi = len(nums)-1
        
#         while lo<hi:
            
#             mid = lo+(hi-lo)//2
            
#             if mid==0:
#                 if nums[mid]<nums[mid+1]:
#                     return nums[mid]
#             elif mid==len(nums)-1:
#                 if nums[mid]<nums[mid-1]:
#                     return nums[mid]
#             else:
#                 if nums[mid]<nums[mid+1] and nums[mid]<nums[mid-1]:
#                     return nums[mid]
                
#             if nums[lo]<=nums[mid] and nums[hi]>nums[mid]:
#                 hi=mid-1
#             elif nums[lo]>=nums[mid] and nums[hi]>nums[mid]:
#                 hi = mid-1
#             elif nums[lo]<=nums[mid] and nums[hi]<nums[mid]:
#                 lo = mid+1
                
#         return nums[lo]
