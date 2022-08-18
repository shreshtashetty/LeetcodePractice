# 720. Longest Word in Dictionary

class Solution:
    def longestWord(self, words: List[str]) -> str:
        
        words = sorted(words)
        
        ind = 0
        
        while ind<len(words) and len(words[ind])>1:
            ind+=1

        if ind>=len(words) or len(words[ind])>1:
            return ""
        
        seen = {words[ind]:1}
        min_len = 1
        max_len = 0
        
        for i in range(ind,len(words)):
            
            if words[i][:-1] in seen:
                seen[words[i]] = len(words[i])
                max_len = max(max_len, len(words[i]))
                
            if len(words[i])==min_len:
                seen[words[i]] = len(words[i])
                
                
        for k, v in seen.items():
            
            if v==max_len:
                return k
            
        return words[0]
