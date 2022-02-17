// 39. Combination Sum

class Solution {
public:
    vector<vector<int>> backtrack(vector<int>& candidates, int& target, vector<vector<int>>& res, vector<int>& arr){
        if(target<0)
            return res;
        
        if(target==0){
            //checks if a vector exists in a vector of vectors
            auto it = find(res.begin(), res.end(), arr);
            if(it == res.end())
                res.push_back(arr);
            return res;
        }
        
        for(int i=0;i<candidates.size();i++){
            arr.push_back(candidates[i]);
            target -= candidates[i];
            //slices the vector
            vector<int> v(candidates.begin()+i, candidates.end());
            res = backtrack(v, target, res, arr);
            target += candidates[i];
            arr.pop_back();
        }
        return res;
    }
    
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>> res;
        vector<int> arr;
        res = backtrack(candidates, target, res, arr);
        return res;
    }
};
