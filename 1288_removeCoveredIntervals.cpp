// 1288. Remove Covered Intervals

class Solution {
public:
    int removeCoveredIntervals(vector<vector<int>>& intervals) {
        if(intervals.size()<2)
            return intervals.size();
            
        sort(intervals.begin(), intervals.end());
        
        int p1 = 0;
        int p2 = 1;
        
        while(p2<intervals.size()){
            if(intervals[p2][0]<=intervals[p1][1] && intervals[p2][1]<=intervals[p1][1]){
                intervals.erase(intervals.begin()+p2);
                continue;
            }
            else if(intervals[p1][0]==intervals[p2][0] && intervals[p1][1]<=intervals[p2][1]){
                intervals.erase(intervals.begin()+p1);
                continue;
            }
            p1+=1;
            p2+=1;
        }
        
        return intervals.size();
    }
};
