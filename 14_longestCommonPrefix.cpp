// 14. Longest Common Prefix

class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        
        if(strs.size()==1)
            return strs[0];
        
        int min_l = INT_MAX-1;
 
        for(int i=0;i<strs.size();i++)
            min_l = min(min_l, (int)strs[i].length());
            
        int p = 0;
        int i;
        for(i=0;i<min_l;i++){
            char c = strs[0][i];
            for(int j=1;j<strs.size();j++){
                if(strs[j][i]!=c)
                {
                    int l = (int)(strs[j]).length();
                    return strs[j].substr(0,i);
                }
                    
            }
        }
        
        return strs[0].substr(0,i);
        
    }
};
