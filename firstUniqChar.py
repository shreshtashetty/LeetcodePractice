# 387. First Unique Character in a String

class Solution:
    def firstUniqChar(self, s: str) -> int:
        ind = -1
        occ = {}
        
        for i in range(len(s)):
            if s[i] not in occ:
                occ[s[i]] = 1
            else:
                occ[s[i]]+=1
        
        for i in range(len(s)):
            if occ[s[i]]==1:
                ind = i
                break
            
        return ind
        
        
