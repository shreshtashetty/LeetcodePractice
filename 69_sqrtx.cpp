// 69. Sqrt(x)

class Solution {
public:
    int mySqrt(int x) {
        if(x==0 || x==1)
            return x;
        
        int l = 0;
        int r = x;
        int ans = 0;
        
        while(l<=r){
            
            int mid = l + (r-l)/2;
            int x_sqrt = x/mid;
            
            if(mid==x_sqrt)
                return mid;
            
            if(mid<x_sqrt){
                l = mid+1;
            }
            else{
                ans = x_sqrt;
                r = mid-1;
            }
        }
        
        return ans;
    }
};
