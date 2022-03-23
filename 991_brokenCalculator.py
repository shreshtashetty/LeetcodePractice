# 991. Broken Calculator

# Refer to their Solution. Work backwards. We always greedily divide by 2 and add 1 only if number is odd.
    
class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        
        ans = 0
        
        while target>startValue:
            ans+=1
            if target%2: target+=1
            else: target//=2
                
        return ans + startValue-target
