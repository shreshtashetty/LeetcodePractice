# 349. Intersection of Two Arrays

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        set1 = set(nums1)
        set2 = set(nums2)
        
        if len(set1)>=len(set2):
            return [n for n in set2 if n in set1]
        else: 
            return [n for n in set1 if n in set2]
