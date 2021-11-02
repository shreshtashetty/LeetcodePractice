# 66. Plus One

from collections import deque

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        ind = len(digits)-1
        num = 1
        
        while(True):
            
            if ind<0:
                break
                
            sum_ = digits[ind] + num
            
            if sum_<9:
                digits[ind] = sum_
                return digits
            else:
                digits[ind] = sum_%10
                ind-=1
                num = sum_//10
                
        l = deque()
        
        while(num>0):
            
            dig = num%10
            l.appendleft(dig)
            num = num//10
            
        l = list(l)
        l+=digits
        
        return l
