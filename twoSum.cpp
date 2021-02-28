class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::vector<int> sol;
        for(int i=0;i<nums.size();i++){
            int num1 = nums[i];
            int num2 = target - num1;
            for(int j=i+1;j<nums.size();j++){
                if(num2==nums[j]){
                    sol.push_back(i);
                    sol.push_back(j);
                }
            }
        }
        return sol;
        
    }
};

