# 131. Palindrome Partitioning

def checkPal(s):
    if len(s)%2==0:
        p1 = (len(s)//2)-1
        p2 = len(s)//2
    else:
        # print(s, len(s))
        p1 = (len(s)//2)
        p2 = (len(s)//2)
        # print(p1,p2)
        
    while p1>=0 and p2<=len(s)-1:
        if s[p1]==s[p2]:
            p1-=1
            p2+=1
        else:
            return False
    return True
        

# def getParts(s, palparts):
#     if len(s)==1:
#         if s not in palparts:
#             palparts.append(s)
#         return        
    
#     for i in range(1,len(s)):
#         getParts(s[:i], palparts)
#         if checkPal(s[:i]) and s[:i] not in palparts:
#             palparts.append(s[:i])
#         getParts(s[i:], palparts)
#         if checkPal(s[i:]) and s[i:] not in palparts:
#             palparts.append(s[i:])
            
#     return
    
def getParts(s, palparts, part, i, l):
    if i>=l:
        palparts.append(part.copy())
        return
    
    for j in range(i,l):
        if checkPal(s[i:j+1]):
            part.append(s[i:j+1])
            getParts(s, palparts, part, j+1, l)
            part.pop()
    
    return    

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        palparts = []
        part = []
        getParts(s, palparts, part, 0, len(s))
        return palparts
