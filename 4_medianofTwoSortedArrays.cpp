//4. Median of Two Sorted Arrays
class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        std::vector <int> combined;
        int iter1 = 0;
        int iter2 = 0;

        while(iter1<nums1.size() && iter2<nums2.size()){
            if(nums1[iter1]<=nums2[iter2]){
                combined.push_back(nums1[iter1]);
                iter1+=1;
            }
            else{
                combined.push_back(nums2[iter2]);
                iter2+=1;
            }
        }

        if(iter1<nums1.size()){
            for(int i=iter1;i<nums1.size();i++){
                combined.push_back(nums1[i]);
            }
        }
        if(iter2<nums2.size()){
            for(int i=iter2;i<nums2.size();i++){
                combined.push_back(nums2[i]);
            }
        }

        for(int i=0;i<combined.size();i++){
            cout<<combined[i]<<" ";
        }
        cout<<endl;
        double med;
        if(combined.size()%2!=0){
            med = combined[combined.size()/2];
        }
        else{
            med = (combined[(combined.size()/2)-1]+combined[(combined.size()/2)])/2.0;
        }
        return med;
    }
};
