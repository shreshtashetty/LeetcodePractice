# 496. Next Greater Element I

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        hash_map = {}
        stack = []
        
        for n in nums2:
            while stack and stack[-1]<n:
                hash_map[stack.pop()] = n
                
            stack.append(n)
            
        for i, n in enumerate(nums1):
            nums1[i] = hash_map.get(n, -1)
            
        return nums1
        
        '''
        
        for i, n in enumerate(nums2):
            
            hash_map[n] = i
            
        for i, n in enumerate(nums1):
            
            ind = hash_map[n] + 1
            great = -1
            
            while ind<len(nums2) and great<n:
                great = nums2[ind]
                ind+=1
                
            if ind<=len(nums2) and great>n:
                nums1[i] = great
            else:
                nums1[i] = -1
                
        return nums1
        
        '''
