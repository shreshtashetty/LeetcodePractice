# 295. Find Median from Data Stream

# Neetcode: https://www.youtube.com/watch?v=itmhHWaHupI

import heapq

class MedianFinder:

    def __init__(self):
        # Keep 2 heaps, a small heap for smaller elements and a large heap for           # larger elements. Small is a maxHeap while large is a minHeap.
        # since python doesn't let us implement a maxHeap, we use a minHeap but           # add -1*(the element) to small.
        self.small, self.large = [], []
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)
        
        # The greatest element in small has to be less than the smallest element         # in large.
        if self.small and self.large and -self.small[0]>self.large[0]:
            val = heapq.heappop(self.small)
            heapq.heappush(self.large, -val)
        
        # The difference between the heap sizes cannot exceed 1. If that happens,         # then shift an element from the heap with the larger size to the one             # with a smaller size.
        if abs(len(self.small)-len(self.large))>1:
            if len(self.small)>len(self.large):
                val = heapq.heappop(self.small)
                heapq.heappush(self.large, -val)
            else:
                val = heapq.heappop(self.large)
                heapq.heappush(self.small, -val)
        

    def findMedian(self) -> float:
        # In case of odd number of elements, one heap have a greater length than         # the other. So in that case return the element on top of the larger             # heap.
        if len(self.small)>len(self.large):
            return -self.small[0]
        if len(self.large)>len(self.small):
            return self.large[0]
        # In case of even number of elements, both the heaps will be of the same         # size, so return the average of the elements on top of both the heaps.
        return (-self.small[0]+self.large[0])/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
