# 219. Contains Duplicate II

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        hash_map = {}
        
        for i in range(len(nums)):
            if nums[i] not in hash_map:
                hash_map[nums[i]] = [i]
            else:
                hash_map[nums[i]].append(i)
                
        
        for key in hash_map.keys():
            if len(hash_map[key])>1:
                p1 = 0
                p2 = len(hash_map[key])-1
                
                while p1<p2:
                    if hash_map[key][p2]-hash_map[key][p1]>k:
                        p1+=1
                        if p1<p2 and hash_map[key][p2]-hash_map[key][p1]<=k:
                            return True
                        else:
                            p2-=1
                    else:
                        return True
                    
        return False
