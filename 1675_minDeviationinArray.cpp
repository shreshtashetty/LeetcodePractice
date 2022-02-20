// 1675. Minimize Deviation in Array

// Basic Explanation: https://www.youtube.com/watch?v=u0n-6zBnohY

class Solution {
public:
    int minimumDeviation(vector<int>& nums) {
        priority_queue <int> heap;
        int min_elem = INT_MAX;
        
        for(int i=0;i<nums.size();i++){
            if(nums[i]%2!=0)
                nums[i]*=2;
            heap.push(nums[i]);
            min_elem = min(min_elem, nums[i]);
        }    
        
        int max_elem = heap.top();
        heap.pop();
        int min_dev = INT_MAX;
        
        while(max_elem%2==0){
            min_dev = min(min_dev, max_elem-min_elem);
            heap.push(max_elem/2);
            min_elem = min(min_elem, max_elem/2);
            max_elem = heap.top();
            heap.pop();
        }
        return min(min_dev, max_elem-min_elem);
        
    }
};
