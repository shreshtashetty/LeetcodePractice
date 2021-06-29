# 125. Valid Palindrome

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = s.lower()
        s = s.replace('_', '') # deal with _ first.
        str_s = ''.join(re.split(r"\W+", s)) # splits when it detects non-alphanumeric chars except _.

        st = 0
        en = len(str_s)-1
        
        while(st<=en):
            if str_s[st]==str_s[en]:
                pass
            else:
                return False
            st+=1
            en-=1
        return True
