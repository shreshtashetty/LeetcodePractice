# 540. Single Element in a Sorted Array

# https://www.youtube.com/watch?v=4Gi8uAz666s

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        
        lo = 0
        hi = len(nums)-1
        
        while lo<hi:

            mid = lo + (hi-lo)//2
            
            if nums[mid]==nums[mid-1]:
                if (hi-mid)%2==0:
                    hi = mid-2
                else:
                    lo = mid+1
                    
            elif nums[mid]==nums[mid+1]:
                if (hi-mid)%2==0:
                    lo = mid+2
                else:
                    hi = mid-1
            else:
                return nums[mid]

        return nums[lo]
