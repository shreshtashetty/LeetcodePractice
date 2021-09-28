# 344. Reverse String

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
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
        
