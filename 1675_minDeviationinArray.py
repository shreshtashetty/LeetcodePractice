# 1675. Minimize Deviation in Array

# Basic Explanation: https://www.youtube.com/watch?v=u0n-6zBnohY

from heapq import *

class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
       
        heap = []
        
        for i in range(len(nums)):
            if nums[i]%2!=0:
                nums[i]*=2
            heap.append(-nums[i])
        
        heapify(heap)
                
        min_elem = min(nums)
        
        max_elem = -1*heappop(heap)
        min_dev = float('inf')
        
        while max_elem%2==0:
            min_dev = min(min_dev, max_elem-min_elem)
            heappush(heap,-max_elem//2)
            min_elem = min(min_elem, max_elem//2)
            max_elem = -1*heappop(heap)
            
        return min(min_dev, max_elem-min_elem)
