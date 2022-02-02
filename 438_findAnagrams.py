# 438. Find All Anagrams in a String

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        ind = 0
        res = []
        
        if len(p)>len(s):
            return []

        from collections import defaultdict
        
        p_map = defaultdict(int)
        
        for i in range(len(p)):
            p_map[p[i]]+=1
      
        s_map = defaultdict(int)
        s_map[s[0]]+=1
        
        for i in range(1,len(s)):
            
            if s_map==p_map:
                res.append(ind)
            s_map[s[i]]+=1
            
            if s_map!=p_map and sum(s_map.values())>=sum(p_map.values()):
                s_map[s[ind]]-=1
                if s_map[s[ind]]==0:
                    s_map.pop(s[ind])
                ind+=1
                
        if s_map==p_map:
            res.append(ind)

#         # BRUTE FORCE APPROACH THAT EXCEEDS TIME LIMIT            
#         for i in range(len(s)):
            
#             if len(s[ind:i+1])==len(p) and sorted(s[ind:i+1])!=p:
#                 ind+=1
#                 continue
                
#             if p==sorted(s[ind:i+1]):
#                 res.append(ind)
#                 ind+=1
                
#             elif s[i] not in p:
#                 ind = i+1
                
        return res
