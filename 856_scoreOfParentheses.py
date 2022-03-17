# 856. Score of Parentheses

# Nick White's Solution: https://www.youtube.com/watch?v=jfmJusJ0qKM

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        score = 0
        
        for i in range(len(s)):
            if s[i]=="(":
                stack.append(score)
                score = 0
            else:
                score = stack.pop() + max(score*2, 1)
        
        return score
                
                
