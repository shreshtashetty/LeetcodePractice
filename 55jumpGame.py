# 55. Jump Game

# Nick White's Solution: https://www.youtube.com/watch?v=Zb4eRjuPHbM

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        lastGoodIndexPosition = len(nums)-1
        
        for i in range(len(nums)-2, -1, -1):
            
            if i+nums[i]>=lastGoodIndexPosition:
                lastGoodIndexPosition=i
                
        if lastGoodIndexPosition==0:
            return True
        else:
            return False
            
        
