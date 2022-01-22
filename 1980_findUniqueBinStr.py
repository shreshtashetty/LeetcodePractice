# 1980. Find Unique Binary String

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        
        # Solution without recursion.
        nums = sorted(nums)
        prev = int(nums[0],2)
        
        if len(nums)==1:
            if nums[0]=="0":
                return "1"
            else:
                return "0"
        
        for i in range(1,len(sorted(nums))):
            
            int_no = int(nums[i],2)
            
            if prev+1<int_no:
                n = bin(prev+1)[2:]
                z = len(nums[i])-len(n)
                return("0"*z+n)
            
            prev = int_no
  
        n = bin(int(nums[-1],2)+1)[2:]
        if len(n)>len(nums):
            n = bin(int(nums[0],2)-1)[2:]
            
        z = len(nums[-1])-len(n)
   
        return "0"*z+n
        
