# 1009. Complement of Base 10 Integer

class Solution:
    def bitwiseComplement(self, n: int) -> int:
        
        bin_rep = bin(n)
       
        compl = bin_rep[0]+bin_rep[1]
        
        for i in range(2,len(bin_rep)):
            if bin_rep[i] =='1':
                compl+= '0'  
            else:
                compl+= '1'
  
        return int(compl,2)
