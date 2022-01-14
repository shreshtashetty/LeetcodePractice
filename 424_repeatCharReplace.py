# 424. Longest Repeating Character Replacement

# Neetcode: https://www.youtube.com/watch?v=gqXU1UyA8pk

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        count = {}
        letters = set(s)
        for i in letters:
            count[i] = 0
        
        p1 = 0
        maxlen = 0
        
        for i in range(len(s)):
            
            count[s[i]]+=1
            
            max_cnt = max(count.values())
            
            num_repl = len(s[p1:i+1])-max_cnt
            
            if num_repl<=k and len(s[p1:i+1])>maxlen:
                maxlen = len(s[p1:i+1])
            
            if num_repl>k:
                count[s[p1]]-=1
                p1+=1
        
        return maxlen
                
