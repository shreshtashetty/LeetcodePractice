# 11. Container With Most Water

class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = -1
        
        p1 = 0
        p2 = len(height)-1
        
        while(p1<p2):
            
            ar = min(height[p1], height[p2])*(p2-p1)
            area = max(area, ar)
            
            if height[p1]<height[p2]:
                p1+=1
            else:
                p2-=1
                
        return area
