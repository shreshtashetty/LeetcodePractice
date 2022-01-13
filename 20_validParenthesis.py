# 20. Valid Parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = deque()
        if len(s)<=1:
            return False
        
        for i in range(len(s)):
            
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                stack.appendleft(s[i])
                
            if s[i] == ')':
                if not stack: return False
                if stack.popleft()!='(':
                    return False
                
            elif s[i] == ']':
                if not stack: return False
                if stack.popleft()!='[':
                    return False
                
            elif s[i] == '}':
                if not stack: return False
                if stack.popleft()!='{':
                    return False
                
        if stack:
            return False
        
        return True
        
