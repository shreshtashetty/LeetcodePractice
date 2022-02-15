// 136. Single Number

class Solution {
public:
    int singleNumber(vector<int>& nums) {
        /*
        // USING UNORDERED MAP FOR HASHMAP
        
        unordered_map<int, int> hashmap;
        for(int a:nums){
            hashmap[a]+=1;
        }
        
        for(auto it=hashmap.begin();it!=hashmap.end();it++)
            if(it->second==1) return it->first;
        
        return -1;
        */
        
/*
GIVES THE FASTEST RUNTIME AND CONSTANT SPACE.
Bitwise XOR Operator(^) has three properties:

a^a = 0
0^a = a
XOR is associative just like addition, multiplication, etc which means that -> a^b^c = a^(b^c) = (a^b)^c = (a^c)^b
So, when we XOR all the numbers in the list, all the numbers that occur 2 times become 0 as a^a = 0. At the end, we will be left with an expression like 0^n, where n is the only number occurring once. Using second property 0^a = a :- 0^n = n. Hence, we get the unique number.
        */
        int resultXOR = 0;
        for(int a:nums)
            resultXOR^=a;
        
        return resultXOR;
        
    }
};
