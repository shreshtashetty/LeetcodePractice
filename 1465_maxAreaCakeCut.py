# 1465. Maximum Area of a Piece of Cake After Horizontal and Vertical Cut

class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.append(0)
        horizontalCuts.append(h)
        horizontalCuts.sort()

        verticalCuts.append(0)
        verticalCuts.append(w)
        verticalCuts.sort()
        
        max_hdiff = 0
        max_vdiff = 0
        for i in range(len(horizontalCuts)-1):
            diff = horizontalCuts[i+1]-horizontalCuts[i]
            if(diff>max_hdiff):
                max_hdiff = diff
                
        for i in range(len(verticalCuts)-1):
            diff = verticalCuts[i+1]-verticalCuts[i]
            if(diff>max_vdiff):
                max_vdiff = diff
                
        return (max_hdiff*max_vdiff)%1000000007
