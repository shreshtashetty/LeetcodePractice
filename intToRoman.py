# 12. Integer to Roman

from collections import deque

class Solution:
    def intToRoman(self, num: int) -> str:
        
        i = 0
        roman = ''
        digits = deque([])
        num_=num
        
        while(num_!=0):
            
            dig = num_%10
            digits.appendleft(dig)
            num_ = num_//10
        
        n = len(digits)-1
        
        while(digits):

            dig = (digits.popleft())*(10**n)
            
            if dig>0 and dig<4:
                while(dig>0):
                    roman+='I'
                    dig-=1
                    
            elif dig==4:
                roman+='IV'
               
            elif dig>=5 and dig<9:
                roman+='V'
                dig-=5
                while(dig>0):
                    roman+='I'
                    dig-=1
                    
            elif dig==9:
                roman+='IX'
            
            elif dig>=10 and dig<40:
                while(dig>0):
                    roman+='X'
                    dig-=10
                    
            elif dig==40:
                roman+='XL'
            
            elif dig>=50 and dig<90:
                roman+='L'
                dig-=50
                while(dig>0):
                    roman+='X'
                    dig-=10
            
            elif dig==90:
                roman+='XC'
                
            elif dig>=100 and dig<400:
                while(dig>0):
                    roman+='C'
                    dig-=100
            
            elif dig==400:
                roman+='CD'
                
            elif dig>=500 and dig<900:
                roman+='D'
                dig-=500
                while(dig>0):
                    roman+='C'
                    dig-=100
            
            elif dig==900:
                roman+='CM'
                
            elif dig>=1000:
                while(dig)>0:
                    roman+='M'
                    dig-=1000
            
            n-=1
            
        return roman
                
            
        
