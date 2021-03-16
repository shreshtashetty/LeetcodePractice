# 1200. Minimum Absolute Difference

# Sort array first. Comparing and appending becomes a lot easier

import numpy as np

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        min_diff = np.inf
        arr = sorted(arr)

        pairs = []
        
        for i in range(len(arr)-1):
            if abs(arr[i]-arr[i+1])<min_diff:
                min_diff = abs(arr[i]-arr[i+1])
                pairs = []
                pairs.append([arr[i], arr[i+1]])
            elif abs(arr[i]-arr[i+1])==min_diff:
                pairs.append([arr[i], arr[i+1]])
        return pairs
