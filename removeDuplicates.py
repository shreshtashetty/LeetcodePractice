# 26. Remove Duplicates from Sorted Array

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        elems = set()
        start = 0
        
        for i in range(len(nums)):
            if nums[i] not in elems:
                elems.add(nums[i])
                
        count = 0
        elems = sorted(elems)
        for i in elems:
            nums[count] = i
            count+=1
        return len(elems)

        
            
            
        
