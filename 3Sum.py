# 15. 3Sum

# Nick White's solution: https://www.youtube.com/watch?v=qJSPYnS35SE

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        triplets = []
        
        if len(nums)<3:
            return triplets
        
        nums = sorted(nums)

        for i in range(len(nums)-2):
            
            low = i+1
            high = len(nums)-1
            twoSum = -nums[i]
            
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
                    
                
            
