# 217. Contains Duplicate

# Both Solutions give the same run time and memory usage!!

import numpy as np
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums = np.array(nums)
        occ = set()
        for i in range(len(nums)):
            if(nums[i] not in occ):
                occ.add(nums[i])
            else:
                return True
        return False
    
        # for i in range(len(nums)):
        #     occ = np.where(nums[i+1:]==nums[i])[0]
        #     if(len(occ)>=1):
        #         return True
        # return False
