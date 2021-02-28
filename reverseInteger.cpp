//7. Reverse Integer
#include <vector>
#include <math.h>

class Solution {
public:
    int reverse(int x) {
        if(x<=-pow(2,31)||x>=pow(2,31)-1) return 0;
        std::vector <int> num;
        int rev=0;
        int rem;
        int copy_x;
    
        
        if(x<0){
            copy_x = x*-1;
        }
        else{
            copy_x = x;
        }
        
        while(copy_x>0){
            rem = copy_x%10;
            num.push_back(rem);
            copy_x=copy_x/10;
        }

        int l = num.size()-1;
        cout<<num.size();
        cout<<endl;
        int n = 0;
        while(l>=0){
            rev+=num[n]*pow(10,l);
            l-=1;
            n+=1;
        }
        if(x<0){
            rev=rev*-1;
        }
        
        if(x>0 && rev<0 || x<0 && rev>0){
            rev = 0;
        }
        return rev;
    }
};
