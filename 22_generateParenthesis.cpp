// 22. Generate Parentheses

vector<string> backtrack(vector<string> res, string curr, int open_, int close_, int n){
    if(curr.length()==n*2){
        res.push_back(curr);
        return res;
    }
    
    if(open_<n)
        res = backtrack(res, curr+"(", open_+1, close_, n);
    if(close_<open_)
        res = backtrack(res, curr+")", open_, close_+1, n);
    
    return res;
}

class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> res;
        res = backtrack(res, "", 0, 0, n);
        return res;
    }
};
