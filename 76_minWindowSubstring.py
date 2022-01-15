# 76. Minimum Window Substring

# Neetcode's Explanation: https://www.youtube.com/watch?v=jSto0O4AJbM

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if t=="": return ""
        
        countT, window = {}, {}
        for c in t:
            countT[c] = 1+countT.get(c, 0)
            
        have, need = 0, len(countT)
        res, reslen = [-1,-1], float("infinity")
        l = 0
        
        for r in range(len(s)):
            
            c = s[r]
            window[c] = 1+window.get(c, 0)
            
            if c in countT and window[c]==countT[c]:
                have+=1
                
            while have==need:
                
                if (r-l+1)<reslen:
                    res = [l, r]
                    reslen = r-l+1
                    
                window[s[l]]-=1
                
                if s[l] in countT and window[s[l]]<countT[s[l]]:
                    have-=1
                l+=1
                
        l, r = res
        
        return s[l:r+1] if reslen!=float("infinity") else ""
