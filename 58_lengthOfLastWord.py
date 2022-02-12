# 58. Length of Last Word

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()
        if len(words)<1:
            return 0
        else:
            return len(words[-1])
        
