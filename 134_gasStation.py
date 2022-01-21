# 134. Gas Station

# Neetcode's explanation: https://www.youtube.com/watch? v=lJwbPZGo05A&list=TLPQMjEwMTIwMjKs2LHeh6yqxA&index=3

import numpy as np

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        if sum(gas)<sum(cost):
            return -1
        
        start = 0
        total = 0
        
        for i in range(len(cost)):
            total+=gas[i]-cost[i]
            if total<0:
                if i<len(cost)-1:
                    start = i+1
                else:
                    start = 0
                total=0
        return start
                
