# 33. Search in Rotated Sorted Array

'''
Idea: There are three cases for when we search on the right half of each step.

If target is between mid and right (easiest case, we know it might be in the right half b/c target is greater than mid but less than right)
If target is greater than mid, and left is less than/equal to mid (even though right will be less than mid, we know it's not in the left half as left is smaller than mid)
If target is less than left, and left is less than/equal to mid (left is smaller than mid, we know it's not in the left half as target is smaller than left)
**left = nums[l], right = nums[r], mid = nums[mid].

Case 1 relies on the proof that target can only be in right half. Cases 2 and 3 relies on the proof that target can not be in left half. Each case also relies on the precondition that the array is strictly increasing (from some index i to n - 1 and continued from 0 to i - 1).

Small example is listed for each case below in form of # [nums], target
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif (nums[mid] < target <= nums[r] or # eg. [2, 0, 1],    1 (0 < 1)
                  nums[l] <= nums[mid] < target or # eg. [1, 2, 3, 0], 3 (1 <= 2)
                  target < nums[l] <= nums[mid]):  # eg. [1, 2, 0],    0 (1 <= 2)
                l = mid + 1
            else:
                r = mid - 1
        return -1
    
    
#  # MY SOLUTION: TAKES SAME AMOUNT OF TIME, BUT VERY SHABBY CODE.    

# def findMin(nums):
    
#     lo = 0
#     hi = len(nums)-1
    
#     while lo<hi:
#         mid = lo + (hi-lo)//2

#         if mid==0:
#             if nums[mid]<nums[mid+1]:
#                 return mid
#         elif mid==len(nums)-1:
#             if nums[mid]<nums[mid-1]:
#                 return mid
#         else:
#             if nums[mid]<nums[mid+1] and nums[mid]<nums[mid-1]:
#                 return mid

#         if nums[lo]<=nums[mid] and nums[hi]>nums[mid]:
#             hi=mid-1
#         elif nums[lo]>=nums[mid] and nums[hi]>nums[mid]:
#             hi = mid-1
#         elif nums[lo]<=nums[mid] and nums[hi]<nums[mid]:
#             lo = mid+1
    
#     return lo

# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
        
#         lo = 0
#         hi = len(nums)-1
#         mid = findMin(nums)

#         if nums[mid]==target:
#             return mid
        
#         if nums[lo]>nums[hi]:
#             if target>nums[mid] and target<=nums[hi]:
#                 lo = mid+1
#             elif target>=nums[lo] and target<=nums[mid-1]:
#                 hi = mid-1

#         while lo<hi:
#             mid = (lo+hi)//2
#             if nums[mid]==target:
#                 return mid
            
#             if nums[mid]>target:
#                 hi = mid-1
#             else:
#                 lo = mid+1

#         return lo if nums[lo]==target else -1
