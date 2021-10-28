# 5. Longest Palindromic Substring

# Nick White's Solution: https://www.youtube.com/watch?v=y2BD4MJqV20

def expandFromCenter(s, left, right):
    
    if not s or left>right:
        return 0
    
    while(left>=0 and right<len(s) and s[left]==s[right]):
        
        left-=1
        right+=1
        
    return right-left-1

class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        if not s or len(s)<1:
            return ""
        
        start = 0
        end = 0
        
        for i in range(len(s)):
            
            len1 = expandFromCenter(s, i, i)
            len2 = expandFromCenter(s, i, i+1)
            len_max = max(len1, len2)
            
            if len_max>(end-start):
                
                start = i-((len_max-1)//2)
                end = i+(len_max//2)
                
        return s[start:end+1]
        
        
