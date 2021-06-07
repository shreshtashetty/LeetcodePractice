# 11. Container With Most Water

class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        i = 0
        j = len(height)-1
               
        max_area = 0
        
        while(i<j):
            
            flag1 = 0
            flag2 = 0
            h = min(height[i], height[j])
            w = j-i
            area = h*w
            
            if area>max_area:
                max_area = area
                
            if height[i]<=height[j]:
                for k in range(i+1,j):
                    if height[k]>height[i]:
                        flag1 = 1
                        i=k
                        break
            elif height[j]<height[i]:
                for k in range(j, i, -1):
                    if height[k]>height[j]:
                        flag2 = 1
                        j=k
                        break       
            if flag1==0 and flag2==0:
                break
            
        return max_area
            
            
