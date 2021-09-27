# 278. First Bad Version

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

import numpy as np
class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 1
        high = n
        mid = low + (high-low)//2
        first_bad = np.inf

        while(low<=high):
            if isBadVersion(mid):
                if mid<first_bad:
                    first_bad = mid
                high = mid-1
            else:
                low = mid+1
            mid = low + (high-low)//2
        return first_bad
                    
