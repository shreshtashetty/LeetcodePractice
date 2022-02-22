# 171. Excel Sheet Column Number

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        
        res = 0
        pow_ = len(columnTitle)-1
        
        for c in columnTitle:
            val = ord(c)-ord('A')+1
            res += val*(26**pow_)
            pow_-=1
            
        return res
