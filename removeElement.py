# 27. Remove Element

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums)==0:
            return 0
        if len(nums)==1 and val==nums[0]:
            return 0
        elif len(nums)==1 and val!=nums[0]:
            return 1
        
        start = 0
        end = len(nums)-1
        
        for i in range(len(nums)):
            if nums[i]==val:
                while(nums[end]==val):
                    end-=1
                    if end<0:
                        return 0
                if i >= end:
                    return end+1
                else:
                    nums[i], nums[end] = nums[end], nums[i]
            
