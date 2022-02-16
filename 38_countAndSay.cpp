// 38. Count and Say

class Solution {
public:
    string convertStr(string s){
      
        string res = "";
        auto num = s[0];
        int count = 0;
      
        for(int i=0;i<s.size();i++){
            if(s[i]!=num){
                res+=to_string(count);
                res.push_back(num);
                count = 1;
                num = s[i];
            }
            else
                count+=1;
        }
        res+=to_string(count)+num;
        return res;
    }
    
    string countAndSay(int n) {
      
        string s = "1";
        for(int i=1;i<n;i++){
            s = convertStr(s);
        }
        return s;
        
    }
};
