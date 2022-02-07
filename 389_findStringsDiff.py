# 389. Find the Difference

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        s_ = {}
        for l in s:
            s_[l] = 1+s_.get(l,0)
            
        t_ = {}
        for l in t:
            t_[l] = 1+t_.get(l,0)
            
        for key in t_:
            if key not in s_:
                return key
            elif t_[key]>s_[key]:
                return key
            
