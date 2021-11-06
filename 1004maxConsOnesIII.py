# 1004. Max Consecutive Ones III

# Nick White's solution: https://www.youtube.com/watch?v=97oTiOCuxho

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        i = 0
        j = 0
        
        while(i<len(nums)):
            
            if nums[i]==0:
                k-=1
            
            if k<0:
                if nums[j]==0:
                    k+=1
                j+=1
                
            i+=1
             
        return i-j
        
