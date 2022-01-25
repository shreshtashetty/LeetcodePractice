# 941. Valid Mountain Array

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        
        if len(arr)<3:
            return False
        
        num = max(arr)
        ind = arr.index(num)
        
        if num==arr[0] or num==arr[-1]:
            return False
        
        for i in range(ind):
            if arr[i]>=arr[i+1]:
                return False
            
        for j in range(ind,len(arr)-1):
            if arr[j]<=arr[j+1]:
                return False
            
        return True
            
