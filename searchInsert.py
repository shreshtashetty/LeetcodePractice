# 35. Search Insert Position

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        low = 0
        high = len(nums)-1
        mid = high//2
        
        while(nums[mid]!=target):
            
            if nums[mid]>target:
                high = mid-1
            elif nums[mid]<target:
                low = mid+1
                
            mid = (low+high)//2

            if low>high:
                break
                
        if low>high:
            return low
        else:
            return mid
