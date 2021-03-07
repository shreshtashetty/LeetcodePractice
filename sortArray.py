# 912. Sort an Array
import numpy as np

#---------------MERGE SORT-----------------------------------------------------
def MergeSort(nums):
    if(len(nums)<=1):
        return nums
    import math
    mid = math.floor((0+len(nums)-1)/2)
    left, right = MergeSort(nums[0:mid+1]), MergeSort(nums[mid+1:])
    # print(left, right)
    res = Merge(left, right)

    return res

def Merge(arr1 = [1, 5, 8, 15, 18, 25], arr2 = [2, 4, 10, 20, 21, 22]):
    result = []
    l_point = 0
    r_point = 0

    while(l_point<len(arr1) and r_point<len(arr2)):
        if(arr1[l_point]<=arr2[r_point]):
            result.append(arr1[l_point])
            l_point+=1
        elif(arr1[l_point]>arr2[r_point]):
            result.append(arr2[r_point])
            r_point+=1

    if(l_point<=len(arr1)-1):
        result.extend(arr1[l_point:])
    elif(r_point<=len(arr2)-1):
        result.extend(arr2[r_point:])

    return result
#--------------------HEAP SORT----------------------------------------------------
def HeapSort(nums):

    for i in range(1, len(nums)): #Keep inserting elements to the heap
        convertToHeapUp(nums, i)
    # print(nums)
    # print("\n")
        
    for i in range(len(nums)-1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        # print(nums)
        # print("\n")
        convertToHeapDown(nums, 0, i)
        
    return nums

def convertToHeapUp(arr, i):
    root = (i+1)//2
    if(root>0 and arr[i]>arr[root-1]):
        arr[i], arr[root-1] = arr[root-1], arr[i]
        convertToHeapUp(arr, root-1)
        
def convertToHeapDown(arr, start, i):
    t = start
    l = 2*start+1
    r = 2*start+2
    
    if(l<i and arr[l]>arr[t]):
        t = l
    if(r<i and arr[r]>arr[t]):
        t = r
    if(t!=start):
        arr[start], arr[t] = arr[t], arr[start]
        convertToHeapDown(arr, t, i)
    
#-----------QUICKSORT---------------------------------------------------------
def partition(arr, low, high):
    i = (low-1)         # index of smaller element
    pivot = arr[high]     # pivot
 
    for j in range(low, high):
 
        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:
 
            # increment index of smaller element
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
 
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)

def QuickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
 
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)
 
        # Separately sort elements before
        # partition and after partition
        QuickSort(arr, low, pi-1)
        QuickSort(arr, pi+1, high)

def quickSort(arr):
    n = len(arr)
    QuickSort(arr, 0, n-1)
    return arr
#----------------------------------------------------------------------------------------
        
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # arr = HeapSort(nums)
        arr = quickSort(nums)
        return arr
        # res  = MergeSort(nums)
        # return res
      
#--------------------INSERTION SORT-----------------------------------------------------
#         for i in range(len(nums)):
#             sorted_arr = nums[:i+1]
#             for j in range(len(sorted_arr)-1, 0, -1):
#                 if(nums[j]<nums[j-1]):
#                     nums[j], nums[j-1] = nums[j-1], nums[j]       
#         return nums
# #-----------------------------------------------------------------------------------------
    
