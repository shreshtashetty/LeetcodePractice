// 503. Next Greater Element II

class Solution {
public:
    vector<int> nextGreaterElements(vector<int>& nums) {
        stack<int> st;
        map<int,int> hash_map;
        int bottom;
        
        for(int i=0;i<nums.size();i++){
            while(!st.empty() && nums[st.top()]<nums[i]){
                int ind = st.top();
                hash_map[ind] = i;
                st.pop();
            }
            if(st.empty())
                bottom = i;
            st.push(i);
        }
        
        for(int i=0;i<bottom+1;i++){
            while(!st.empty() && nums[st.top()]<nums[i]){
                int ind = st.top();
                hash_map[ind] = i;
                st.pop();
            }
            st.push(i);
        }
        
        vector<int> ans;
        for(int i=0;i<nums.size();i++)
            ans.push_back(-1);
    
        for(auto i:hash_map)
            ans[i.first] = nums[i.second];
        return ans;
    }
};
