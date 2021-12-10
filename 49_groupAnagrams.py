#49. Group Anagrams
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        s = []
        all_ = []
        
        for i in range(len(strs)):
            a = sorted(strs[i])
            if(a not in s):
                s.append(a)
                group = []
                group.append(strs[i])
                all_.append(group)
            else:
                ind = s.index(a)
                all_[ind].append(strs[i])
        return all_
        
