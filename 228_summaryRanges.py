# 228. Summary Ranges

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        
        if len(nums)==0:
            return nums
        
        if len(nums)==1:
            return [str(nums[0])]
        
        ranges = []
        
        p1 = 0
        
        for i in range(1,len(nums)):
            
            if p1==0 and i==1 and nums[p1]+1!=nums[i]:
                ranges.append(str(nums[p1]))
                p1 = i
                continue
            
            if nums[i-1]+1!=nums[i]:
                if p1==i-1:
                    ranges.append(str(nums[p1]))
                else:
                    ranges.append(str(nums[p1])+"->"+str(nums[i-1]))
                p1 = i
            
        
        if i==len(nums)-1:
            if p1==i:
                ranges.append(str(nums[p1]))
            else:
                ranges.append(str(nums[p1])+"->"+str(nums[i]))
                
        return ranges
        
        
        
