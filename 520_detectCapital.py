# 520. Detect Capital

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        
        caps = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        pos = []
        cnt = 0
        
        for i in range(len(word)):
            if word[i] in caps:
                cnt+=1
                pos.append(i)
                
        if cnt==len(word):
            return True
        
        if cnt==1 and pos[0]==0:
            return True
        
        if cnt==0:
            return True
        
        return False
        
