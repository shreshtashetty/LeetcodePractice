# 167. Two Sum II - Input array is sorted

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        point1 = 0
        point2 = 1
        n = len(numbers)-1
        
        for i in range(len(numbers)-1):
            
            low = i+1
            high = n
            mid = low+((high-low)//2)
            diff = target-numbers[i]
            
            while(low<high):

                if numbers[mid]==diff:
                    break
                elif numbers[mid]>diff:
                    high = mid-1
                elif numbers[mid]<diff:
                    low = mid+1
                
                mid = low+((high-low)//2)
                
                if low>=high:
                    break
                    
            if numbers[mid]==diff:
                return [i+1, mid+1]
            
        
