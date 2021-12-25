# 227. Basic Calculator II

from collections import deque

class Solution:
    def calculate(self, s: str) -> int:
        
        currNum = 0
        operation = '+'
        l = len(s)

        if l==0:
            return 0
        
        stack = deque([])
        
        for i in range(l):
            
            currChar = s[i]
            
            if currChar.isdigit():
                currNum = currNum*10 + int(currChar)
                
            if (not currChar.isdigit() and currChar!=" ") or (i==l-1):
                
                if operation=='-':
                    stack.appendleft(-currNum)
                    
                elif operation=='+':
                    stack.appendleft(currNum)
                    
                elif operation=='*':
                    num = stack.popleft()
                    currNum = num*currNum
                    stack.appendleft(currNum)
                    
                elif operation=='/':
                    num = stack.popleft()
                    currNum = int(num/currNum)
                    stack.appendleft(currNum)
                    
                operation = currChar
                currNum = 0
                
        result = 0
        
        while stack:
            result+=stack.popleft()
            
        return result
                
        
