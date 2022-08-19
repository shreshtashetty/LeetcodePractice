// 720. Longest Word in Dictionary

class Solution {
public:
    string longestWord(vector<string>& words) {
        
        sort(words.begin(), words.end());
        
        int ind = 0;
        
        while(ind<words.size() && (words[ind]).length()>1)
            ind+=1;
        
        if(ind>=words.size() || words[ind].length()>1)
            return "";
        
        map<string, int> seen;
        
        seen = {{words[ind], 1}};
        
        int min_len = 1;
        int max_len = 0;
        
        for(int i=ind;i<words.size();i++){
            
            // map<string,int>::const_iterator exists = seen.find(words[i].substr(0, words[i].length()-1));
            string s = words[i].substr(0, words[i].length()-1);
            
            if(seen.find(s)!=seen.end()){
                seen[words[i]] = words[i].length();
                int l = words[i].length();
                max_len = max(max_len, l);
            }
            
            if(words[i].length()==min_len)
                seen[words[i]] = min_len;      
        
        }
        
        for(const auto& key_value:seen)
            if(key_value.second==max_len)
                return key_value.first;
        
        return words[ind];
        
    }
};
