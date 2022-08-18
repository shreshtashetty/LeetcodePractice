// 581. Shortest Unsorted Continuous Subarray
// Look through Leetcode solutions.

class Solution {
public:
    int findUnsortedSubarray(vector<int>& nums) {
        
        vector<int> nums_copy;
        for(int i=0;i<nums.size();i++)
            nums_copy.push_back(nums[i]);
        
        sort(nums.begin(),nums.end());
        
        int i;
        int j;
        
        for(i=0;i<nums.size();i++)
            if(nums[i]!=nums_copy[i])
                break;
        for(j=nums.size()-1;j>=0;j--)
            if(nums[j]!=nums_copy[j])
                break;
       
        if(i<j)
            return j-i+1;
        else
            return 0;
    }
};
