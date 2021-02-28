#480. Sliding Window Median
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        import math
        i=0
        j=0+k
        median = []
        while(j<=len(nums)):
            arr = sorted(nums[i:j])
            if(len(arr)%2==0):
                ind = int(len(arr)/2)
                med = (arr[ind-1]+arr[ind])/2
            else:
                ind = math.floor(len(arr)/2)
                med = arr[ind]
            median.append(med)
            i+=1
            j+=1
        return median
