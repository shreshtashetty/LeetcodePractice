#164. Maximum Gap

# CODED UP QUICKSORT JUST FOR PRACTICE

class Solution:
    def partition(self, arr, low, high):
        pivot = arr[high]
        final_ind = low-1
        for i in range(low, high):
            if(arr[i]<=pivot):
                final_ind+=1
                arr[final_ind], arr[i] = arr[i], arr[final_ind]
        final_ind+=1
        arr[final_ind], arr[high] = arr[high], arr[final_ind]
        return final_ind
        
    def quickSort(self, arr, low, high):
        if(len(arr)==1):
            return arr
        if(low<high):
            pivot_ind = self.partition(arr, low, high)
            self.quickSort(arr, low, pivot_ind-1)
            self.quickSort(arr, pivot_ind+1, high)
        
    def QuickSort(self, arr):
        n = len(arr)
        self.quickSort(arr, 0, n-1)        
        return arr
        
    def maximumGap(self, nums: List[int]) -> int:
        nums_sorted = self.QuickSort(nums)
        print(nums_sorted)
        max_ind = 0
        for i in range(len(nums_sorted)-1):
            ind = nums_sorted[i+1]-nums_sorted[i]
            if(max_ind<ind):
                max_ind = ind
        return max_ind
        
