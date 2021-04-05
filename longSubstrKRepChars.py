# 395. Longest Substring with At Least K Repeating Characters

import numpy as np

#                     C H E C K   T H I S   L A T E R
#
# def longestSubstringUtil(s, start, end, k):
#     if end<k:
#         return 0
#     countMap = np.zeros(26)
#     for i in range(start, end):
#         # ind = countMap.index(s[i])
#         ind = ord(s[i])-ord('a')
#         countMap[ind]+=1
#     for mid in range(start, end):
#         ind = ord(s[mid])-ord('a')
#         if countMap[ind]>=k:
#             continue
#         midNext = mid+1
#         ind = ord(s[midNext])-ord('a')
#         while(midNext<end and countMap[ind]<k):
#             ind = ord(s[midNext])-ord('a')
#             midNext+=1
#         return max(longestSubstringUtil(s, start, mid, k),
#                   longestSubstringUtil(s, midNext, end, k))
#     return end-start

# Solution got from discussion. Also look at later
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0  
        # print(s.count)
        c = min(set(s), key=s.count)
        if s.count(c) >= k:
            return len(s)
        return max(self.longestSubstring(t, k) for t in s.split(c))
        # return longestSubstringUtil(s, 0, len(s), k)
    
    
