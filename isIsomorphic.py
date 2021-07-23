# 205. Isomorphic Strings

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_t = {}
        t_s = {}
        
        for i in range(len(s)):
            if s[i] not in s_t and t[i] not in t_s:
                s_t[s[i]] = t[i]
                t_s[t[i]] = s[i]
            elif s[i] not in s_t and t[i] in t_s:
                return False
            elif s[i] in s_t and t[i] not in t_s:
                return False
            elif s[i] not in s_t and t[i] in t_s:
                return False
            elif s[i] in s_t and t[i] in t_s:
                if s_t[s[i]]!=t[i] or t_s[t[i]]!=s[i]:
                    return False
        
        return True
        
        
