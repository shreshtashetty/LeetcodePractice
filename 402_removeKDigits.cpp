// 402. Remove K Digits

class Solution {
public:
    string removeKdigits(string num, int k) {
        if(num.length()==1)
            return "0";
        
        vector<string> stack;
        
        int i=0;
        
        for(i=0;i<num.length();i++){
            
            string s(1,num[i]);
            
            if(stack.empty() || stoi(stack.back())<=stoi(s)){
                stack.push_back(s);
                
            }
            
            else if(stoi(stack.back())>stoi(s)){
                while(!stack.empty() && stoi(stack.back())>stoi(s) && k>0){
                    stack.pop_back();
                    k-=1;
                }
                stack.push_back(s);
            }
            
            if(k==0)
                break;
            
        }

        
        if(stack.size()==num.length()){
            
            if(num.length()-k<=0)
                return "0";
            string r = num.substr(0,num.length()-k);
            string s(1,r[0]);
            while(s=="0"){
                s = r.substr(1,r.length()-1);
                s = r[0];
            }
            if(r=="")
                return "0";
            return r;
        }
        
        string res = "";
        for(string s:stack){
            res+=s;
        }
            
        
        if(k>0){

            if(k>=res.length())
                return "0";
            
            int n1 = stoi(res.substr(0,res.length()-k));
            int n2 = stoi(res.substr(k,res.length()-k));

            if(n1<n2)
                return to_string(n1);
            else
                return to_string(n2);
        }
        
        if(i==num.length()-1)
        {
            string l(1,res[0]);
            while(l=="0"){
                res = res.substr(1,res.length()-1);
                l = res[0];
            }
            if(res=="")
                return "0";
            return res;
        }
            
        else{
            res = res+num.substr(i+1,num.length()-(i+1));
           
            string s(1,res[0]);
            while(s=="0"){
                res = res.substr(1,res.length()-1);
                s = res[0];
            }
            if(res=="")
                return "0";
            return res;
        }
            
    }
};
