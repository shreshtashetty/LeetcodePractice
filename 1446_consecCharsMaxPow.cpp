// 1446. Consecutive Characters

class Solution {
public:
    int maxPower(string s) {
        
        vector<int> v;
        
        for(int i=0;i<s.length();i++){
            
            if(i==0 || s[i]!=s[i-1])
                v.push_back(1);
            else{
                v.back() = v.back()+1;
            }
        }
        
        int max_val = 0;
        
        for(int i=0;i<v.size();i++){
            
            if(v.at(i)>max_val)
                max_val = v.at(i);
        }
        
        return max_val; 
    }
};
