# 43. Multiply Strings

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        i, j = 0, 0
        n1, n2 = 0, 0
        
        while(i<len(num1)):
            n1 = n1*10 + int(num1[i])
            i+=1
            
        while(j<len(num2)):
            n2 = n2*10 + int(num2[j])
            j+=1
        
        return str(n1*n2)
