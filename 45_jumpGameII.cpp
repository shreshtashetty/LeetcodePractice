// 45. Jump Game II

class Solution {
public:
    // DYNAMIC PROGRAMMING
    int jump(vector<int>& nums) {
        
        vector<int> res;
        
        for(int i=0;i<nums.size();i++)
            res.push_back(INT_MAX-1);
        
        res[nums.size()-1] = 0;
        
        for(int i=nums.size()-1;i>-1;i--){
            for(int j=i+1;j<i+nums[i]+1;j++){
                if(j<nums.size())
                    res[i] = min(res[i], 1+res[j]);  
            }
        }
        
        return res[0];
    }
};
