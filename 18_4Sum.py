# 18. 4Sum

def threeSum(nums, k, three_Sum):

    triplets = []

    for i in range(k, len(nums)-2):

        low = i+1
        high = len(nums)-1
        twoSum = three_Sum-nums[i]

        while(low<high):

            if nums[low]+nums[high]==twoSum:

                if [nums[i], nums[low], nums[high]] not in triplets:
                    triplets.append([nums[i], nums[low], nums[high]])

                while(low<high and nums[low]==nums[low+1]):
                    low+=1

                while(low<high and nums[high]==nums[high-1]):
                    high-=1

                low = low+1
                high = high-1

            elif nums[low]+nums[high]>twoSum:
                high-=1
            else:
                low+=1

    return triplets

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        quads = []

        if len(nums)<4:
            return []
        
        if all(x==0 for x in nums):
 
            if target == 0:
                return [[0]*len(nums)]
            else:
                return []
            
        nums = sorted(nums)
        
        for i in range(len(nums)-3):
  
            three_Sum = target-nums[i]
       
            trip = threeSum(nums, i+1, three_Sum)
    
            for j in range(len(trip)):
                if [nums[i]]+trip[j] not in quads:
                    quads.append([nums[i]]+trip[j])
        return quads
            
            
        
