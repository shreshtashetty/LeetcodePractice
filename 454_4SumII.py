# 454. 4Sum II

'''

# RECURSION SOLUTION. WORKS BUT GIVES TLE. BECAUSE IT IS EXACTLY LIKE THE BRUTE FORCE SOLN # WITH 4 FOR LOOPS.

def recurse(arr, ind, elem_sum,num_tuples):
   
    if ind==len(arr):
        if elem_sum!=0:
            return num_tuples
        else:
            return num_tuples+1
    
    for j in range(len(arr[ind])):
        elem_sum+=arr[ind][j]
        num_tuples = recurse(arr,ind+1,elem_sum,num_tuples)
        elem_sum-=arr[ind][j]
        
    return num_tuples


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        
        arr = [nums1, nums2, nums3, nums4]
        elem_sum,num_tuples = 0,0
        num_tuples = recurse(arr, 0, elem_sum,num_tuples)

        return num_tuples
'''

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        
        hash_map = {}
        
        for i in nums1:
            for j in nums2:
                hash_map[i+j]=1+hash_map.get(i+j, 0)
                
        count = 0        
        for i in nums3:
            for j in nums4:
                count+=hash_map.get(-(i+j),0)
                
        return count
        
        
