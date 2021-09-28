# 567. Permutation in String

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        n_iters = len(s2)-len(s1)+1
        sorted_s1 = sorted(s1)
        l_s1 = len(s1)
        
        for i in range(n_iters):
            substr = s2[i:i+l_s1]
            if sorted_s1 == sorted(substr):
                return True
        return False
