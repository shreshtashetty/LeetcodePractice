# 316. Remove Duplicate Letters

# Anish Malla's explanation: https://www.youtube.com/watch?v=2ayws5Y-WM4

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        
        d = {c:i for i,c in enumerate(s)}
        res = []
        
        for i in range(len(s)):
            if s[i] not in res:
                while res and i<d[res[-1]] and s[i]<res[-1]:
                    res.pop()
                res.append(s[i])
                
        return "".join(res)
        
        
