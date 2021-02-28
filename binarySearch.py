#704. Binary Search
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        first = 0
        last = len(nums)-1
        middle = floor((last+first)/2)
        
        while(nums[middle]!=target):
            if(nums[middle]!=target):
                if(target>nums[middle]):
                    first = middle+1
                else:
                    last = middle-1
                middle = floor((first+last)/2)
            if(first>last):
                return -1
            
        return middle
