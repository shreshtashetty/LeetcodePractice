// 6. Zigzag Conversion

class Solution {
public:
    string convert(string s, int numRows) {
        
        if(numRows==1)
            return s;
        
        vector<vector<char>> l;
        
        for(int i=0;i<numRows;i++){
            vector<char> v;
            l.push_back(v);
        }
        
        int row = 0;
        int direc = 1;
        
        for(int i=0;i<s.length();i++){
            if(direc==-1){
                l[row].push_back(s[i]);
                row-=1;
                if(row<0){
                    row+=2;
                    direc=1;
                    continue;
                }
            }
            if(direc==1){
                l[row].push_back(s[i]);
                row+=1;
                if(row==l.size()){
                    row-=2;
                    direc=-1;
                }
            }
        }
        
        string str2 = "";
        
        for(int i=0;i<l.size();i++){
            string str1 = "";
            for(int j=0;j<l[i].size();j++){
                str1+=l[i][j];
            }
            str2+=str1;
        }
        return str2;
    }
};
