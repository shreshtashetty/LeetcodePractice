// 171. Excel Sheet Column Number

class Solution {
public:
    int titleToNumber(string columnTitle) {
        unordered_map<string, int> hash_map;
        string letters[26] = {"A","B","C","D","E","F","G","H","I","J","K","L","M","N","O"
                         ,"P","Q","R","S","T","U","V","W","X","Y","Z"};
        string s = "";
        int count = 1;
        
        for(int i=0;i<26;i++)
        {
            hash_map[letters[i]] = count;
            count+=1;
        }
        
        int l = columnTitle.length();
        
        int res = 0;
        int pow_ = 0;
        
        for(int j=l-1;j>=0;j--){
            
            string str1(1, columnTitle[j]);
            res+=(hash_map[str1]*pow(26,pow_));
            pow_+=1;
            
        }

        return res;
    }
};
