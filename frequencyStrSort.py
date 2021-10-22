# 451. Sort Characters By Frequency

class Solution:
    def frequencySort(self, s: str) -> str:
        
        hash_map = {}
        
        for i in range(len(s)):
            
            if s[i] not in hash_map:
                hash_map[s[i]] = 1
            else:
                hash_map[s[i]] += 1
        
        desc_hash_map = dict(sorted(hash_map.items(), reverse=True, key=lambda item:item[1]))
        
        s_new = ""
        for k, v in desc_hash_map.items():
            while(v>0):
                s_new+=k
                v-=1
        return s_new
            
