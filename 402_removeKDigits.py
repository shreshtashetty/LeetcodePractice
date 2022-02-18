# 402. Remove K Digits

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        if len(num)==1:
            return "0"
        
        stack = []
        
        for i in range(len(num)):
            
            if not stack or stack[-1]<=num[i]:
                stack.append(num[i])
                
            elif stack[-1]>num[i]:
                while stack and stack[-1]>num[i] and k>0:
                    stack.pop()
                    k-=1
                stack.append(num[i])
               
            if k==0:
                break
        
        if len(stack)==len(num):
            if num[:-k]=="":
                return "0"
            return str(int(num[:-k]))
        
        if k>0:
            res = "".join(stack)
            if res[:-k]=="" or res[k:]=="":
                return "0"
            n1, n2 = int(res[:-k]), int(res[k:])
            return str(n1) if n1<n2 else str(n2)
        

        res = "".join(stack) if i==len(num)-1 else "".join(stack)+num[i+1:]
        return str(int(res))
