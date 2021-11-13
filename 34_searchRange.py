# 34. Find First and Last Position of Element in Sorted Array

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        if not nums:
            return [-1, -1]
        
        if target<nums[0] or target>nums[-1]:
            return [-1, -1]
        
        low = 0
        high = len(nums)-1
        
        while(low<=high):
            mid = low + (high-low)//2
            if nums[mid]==target:
                break
            if nums[mid]>target:
                high = mid-1
            elif nums[mid]<target:
                low = mid+1
                

        if low<=high:
            s = mid
        else:
            return [-1,-1]
        
        e = s+1
  
        while(s>=0):
            if nums[s]!=target:
                break
            else:
                s-=1
        
        while(e<len(nums)):
            if nums[e]!=target:
                break
            else:
                e+=1
                
        return [s+1, e-1]
            
