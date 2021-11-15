# 368. Largest Divisible Subset

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums = sorted(nums)
        seq = []
        
        if len(nums)<2:
            return nums
        
        for i in range(len(nums)-2, -1, -1):
            
            for j in range(i+1, len(nums)):
                
                if nums[j]%nums[i]==0:
                    
                    flag = 0
                    
                    for k in range(len(seq)):
                        
                        if seq[k][0]==nums[j]:
                            
                            flag = 1
                            seq[k].insert(0, nums[i])
                            
                    if flag==0:
                        
                        seq.append([nums[i], nums[j]])

        print(seq)  
        
        if not seq:
            return [nums[0]]
        
        maxlen = -1
        ind = -1
        
        for i in range(len(seq)):
            
            if len(seq[i])>maxlen:
                
                maxlen = len(seq[i])
                ind = i
                
        return seq[ind]
    
