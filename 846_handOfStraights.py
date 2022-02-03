# 846. Hand of Straights

# Neetcode: https://www.youtube.com/watch?v=amnrMCVd2YI

from heapq import *

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        if len(hand)%groupSize!=0:
            return False
        
        count = {}
        
        for i in range(len(hand)):
            count[hand[i]] = count.get(hand[i],0) + 1
        
        minHeap = list(count.keys())
        heapify(minHeap)
        
        while minHeap:
            minVal = minHeap[0]
            for i in range(minVal, minVal+groupSize):
                if i not in count:
                    return False
                count[i]-=1
                if count[i]==0:
                    if i!=minHeap[0]:
                        return False
                    else:
                        heappop(minHeap)
                        
        return True
        
