# 38. Count and Say

def convertStr(s):
    res = ""
    num = s[0]
    count = 0
    for i in range(len(s)):
        if s[i]!=num:
            res+=str(count)+num
            count = 1
            num = s[i]
        else:
            count+=1
    res+=str(count)+num
    return res

class Solution:
    def countAndSay(self, n: int) -> str:
        s = "1"
        for i in range(1,n):
            s = convertStr(s)
         
        return s
            
