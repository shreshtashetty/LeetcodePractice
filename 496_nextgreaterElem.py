# 496. Next Greater Element I

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        ans = [-1]*len(nums1)
        
        hash_map = {}
        
        for i, n in enumerate(nums2):
            
            hash_map[n] = i
            
        for i, n in enumerate(nums1):
            
            ind = hash_map[n] + 1
            great = -1
            
            while ind<len(nums2) and great<n:
                great = nums2[ind]
                ind+=1
                
            if ind<=len(nums2) and great>n:
                ans[i] = great
                
        return ans
