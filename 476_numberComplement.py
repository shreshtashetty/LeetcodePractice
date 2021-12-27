# 476. Number Complement

class Solution:
    def findComplement(self, num: int) -> int:
        binary = list(bin(num))
   
        for i in range(2,len(binary)):
            if binary[i]=='1':
                binary[i] = '0'
            else:
                binary[i] = '1'
                
        compl = ''.join(binary)
        
        return int(compl,2)
