# 56. Merge Intervals

#[[1,3],[2,6],[8,10],[15,18]]
#[[1, 5], [6, 10], [8, 9], [10, 14]]

def Merge2Arrays(arr1, arr2):
    if(arr1[1]<arr2[0]):
        return [arr1, arr2]
    elif(arr1[1]==arr2[0]):
        return [[arr1[0], arr2[1]]]
    elif(arr1[1]>arr2[0]):
        if(arr1[1]<=arr2[1]):
            return [[arr1[0], arr2[1]]]
        else:
            return [arr1]

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key = lambda x:x[0])
        i = 0
        while(i<len(intervals)-1):
            arr = Merge2Arrays(intervals[i], intervals[i+1])
            if(len(arr)==1):
                intervals[i] = arr[0]
                intervals.pop(i+1)
            else:
                i+=1
        return intervals
