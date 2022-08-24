// 496. Next Greater Element I

class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        stack<int> st;
        unordered_map<int,int> hash_map;
        
        for(int i=0;i<nums2.size();i++){
            
            while(!st.empty() && st.top()<nums2[i]){
                int num = st.top();
                hash_map[num] = nums2[i];
                st.pop();
            }

            st.push(nums2[i]);
        }
        
        for(int i=0;i<nums1.size();i++){
            
            if(hash_map.find(nums1[i])!=hash_map.end())
                nums1[i] = hash_map[nums1[i]];
            else
                nums1[i] = -1;
        }
        return nums1;
    }
};
