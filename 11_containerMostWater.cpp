// 11. Container With Most Water

class Solution {
public:
    int maxArea(vector<int>& height) {
        int p1 = 0;
        int p2 = height.size()-1;
        int maxarea = 0;
        
        while(p1<p2){
            maxarea = max(maxarea, (p2-p1)*(min(height[p1],height[p2])));
            if(height[p2]>=height[p1])
                p1+=1;
            else
                p2-=1;
        }
        return maxarea;
    }
};
