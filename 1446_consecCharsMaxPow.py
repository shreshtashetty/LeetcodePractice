# 1446. Consecutive Characters

class Solution:
    def maxPower(self, s: str) -> int:
        
        hash_map = []
        
        for i in range(len(s)):
            
            if i==0 or s[i]!=s[i-1]:
                hash_map.append([s[i], 1])
            else:
                hash_map[-1][1]+=1 
        
        max_val = 0       
        
        for i in range(len(hash_map)):
            
            if hash_map[i][1]>max_val:
                max_val=hash_map[i][1]
        
        return max_val
