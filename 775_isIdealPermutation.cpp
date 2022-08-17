// 775. Global and Local Inversions

class Solution {
public:
    bool isIdealPermutation(vector<int>& nums) {
        
        int min_elem = nums.back();
        
        for(int i=nums.size()-3;i>=0;i--){
            
            if(nums[i]>min_elem)
                return false;
            
            min_elem = min(min_elem,nums[i+1]);
        }
        return true;
    }
};
