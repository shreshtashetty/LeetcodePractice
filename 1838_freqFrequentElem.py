# 1838. Frequency of the Most Frequent Element

'''
[9907, 9907, 9910, 9912, 9914, 9933, 9934, 9937, 9940, 9940, 9941, 9941, 9944, 9944, 9952, 9952, 9964, 9980, 9980, 9987, 9995, 9997] 

[9930,9923,9983,9997,9934,9952,9945,9914,9985,9982,9970,9932,9985,9902,9975,9990,9922,9990,9994,9937,9996,9964,9943,9963,9911,9925,9935,9945,9933,9916,9930,9938,10000,9916,9911,9959,9957,9907,9913,9916,9993,9930,9975,9924,9988,9923,9910,9925,9977,9981,9927,9930,9927,9925,9923,9904,9928,9928,9986,9903,9985,9954,9938,9911,9952,9974,9926,9920,9972,9983,9973,9917,9995,9973,9977,9947,9936,9975,9954,9932,9964,9972,9935,9946,9966]
3056

nums[r]*(r-l+1)<=sum(nums[l:r+1])+k
'''

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        
        max_freq = 1
        
        nums = sorted(nums)
        sum_ = nums[0]
        l = 0
        
        for r in range(1,len(nums)):
            
            sum_+=nums[r]
            
            while nums[r]*(r-l+1)>sum_+k:
                sum_-=nums[l]
                l+=1
                
            max_freq = max(max_freq, r-l+1)
            
        return max_freq
                
            
            
            
        
