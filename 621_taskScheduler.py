# 621. Task Scheduler

# Kevin Naughton Jr's: https://www.youtube.com/watch?v=ySTQCRya6B0

import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        task_occur = {}
        
        for t in tasks:
            if t not in task_occur:
                task_occur[t]=1
            else:
                task_occur[t]+=1
        
        maxHeap = []
        
        for key,value in task_occur.items():
            heapq.heappush(maxHeap,[-value,key])
        
        cycles = 0
        
        while maxHeap:
            temp = []
            for i in range(n+1):
                if maxHeap:
                    temp.append(heapq.heappop(maxHeap))
                    
            for i in range(len(temp)):
                if temp[i][0]+1<0:
                    temp[i][0]+=1
                    heapq.heappush(maxHeap,temp[i])
                    
            if not maxHeap:
                cycles+=len(temp)
            else:
                cycles+=n+1
                
        return cycles
                
