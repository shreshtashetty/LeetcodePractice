# 189. Rotate Array

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        while k>=len(nums):
            k-=len(nums)
        ind_elem = {}
        
        for i in range(len(nums)):
            # print([i-k])
            ind_elem[i]=nums[i-k]
        # print(ind_elem)
        
        for i in range(len(nums)):
            nums[i] = ind_elem[i]            
        
        # # O(n^2)
        # for _ in range(k):
        #     keep_track = nums[-1]
        #     for i in range(len(nums)):
        #         temp = nums[i]
        #         nums[i] = keep_track
        #         keep_track = temp

            
