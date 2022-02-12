# 258. Add Digits

class Solution:
    def addDigits(self, num: int) -> int:
        
        # DIGITAL ROOT
        
        if num<10:
            return num
        
        if num%9==0:
            return 9
        else:
            return num%9
        
        '''
        while num>9:
            digits = 0
            
            while num!=0:
                digits+=num%10
                num = num//10
                
            num = digits

        return num
        
        '''
        
