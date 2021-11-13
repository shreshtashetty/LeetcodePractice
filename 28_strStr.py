# 28. Implement strStr()

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        if not needle:
            return 0
        
        p1 = 0
        l = len(needle)
        p2 = p1+l
        
        while(p2<=len(haystack)):
            
            if needle == haystack[p1:p2]:
                return p1
            else:
                p1+=1
                p2+=1
        
        return -1
            
        
