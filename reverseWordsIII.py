# 557. Reverse Words in a String III

def reverseString(s):
    s = list(s)
    if len(s)%2==0:
        point1 = int((len(s)/2)-1)
        point2 = int(len(s)/2)
    else:
        mid = len(s)//2
        point1 = mid-1
        point2 = mid+1

    while(point1>=0 and point2<=len(s)-1):
        s[point1], s[point2] = s[point2], s[point1]
        point1-=1
        point2+=1
    
    return "".join(s)

class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        revStr = ""
        for i in range(len(words)-1):
            revStr += reverseString(words[i]) + " "
        revStr += reverseString(words[-1])
        return revStr
