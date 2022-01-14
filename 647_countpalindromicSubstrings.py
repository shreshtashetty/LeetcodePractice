# 647. Palindromic Substrings

def expandFromCentre(s, l, r, num_pal):

    while l>=0 and r<=len(s)-1 and s[l]==s[r]:

        num_pal+=1
        l-=1
        r+=1
        
    return num_pal

class Solution:
    def countSubstrings(self, s: str) -> int:
        n_pal = 0
        
        for i in range(len(s)):
            
            n_pal1=expandFromCentre(s, i, i, 0)
            n_pal2=expandFromCentre(s, i, i+1, 0)
            n_pal+=(n_pal1+n_pal2)
        
        return n_pal
        
            
            
            
        
