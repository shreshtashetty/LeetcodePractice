# 735. Asteroid Collision

'''
[5,10,-5]
[-2,-1,1,2]
[-2,-2,1,-2]
[-2,-1,1,-2]
'''
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        stack = []
        
        for a in asteroids:
            if not stack or (stack[-1]<0 and a<0) or (stack[-1]>0 and a>0) or (stack[-1]<0 and a>0):
                stack.append(a)
            else:
                if abs(stack[-1])>abs(a):
                    continue
                elif abs(stack[-1])==abs(a):
                    stack.pop()
                else:
                    flag = 0
                    while stack and abs(stack[-1])<=abs(a):
                        if abs(stack[-1])<abs(a):
                            if (stack[-1]<0 and a<0) or (stack[-1]>0 and a>0) or (stack[-1]<0 and a>0):
                                stack.append(a)
                                flag=0
                                break
                            else:
                                flag = 1 # have to append later
                                stack.pop()
                        elif stack[-1]==a:
                            stack.append(a)
                            flag = 0 # don't have to append
                            break
                        elif abs(stack[-1])==abs(a) and stack[-1]!=a:
                            flag = 0
                            stack.pop()
                            break
                            
                    if stack and abs(stack[-1])>abs(a) and abs(stack[-1]+a)!=abs(stack[-1])+abs(a):
                        flag = 0
                    if flag==1:
                        stack.append(a)
                    
        return stack
                    
