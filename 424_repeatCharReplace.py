# 424. Longest Repeating Character Replacement

# Neetcode: https://www.youtube.com/watch?v=gqXU1UyA8pk

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l = 0
        
        count = {}
        res = 0
        
        for i in range(len(s)):
            
            count[s[i]] = 1 + count.get(s[i], 0)
            
            while (i-l+1)-max(count.values())>k:
                count[s[l]]-=1
                l+=1
            
            res = max(res, i-l+1)
            
        return res
