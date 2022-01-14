#49. Group Anagrams
'''
# A less efficient solution
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
 '''

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        l = []
        
        for i in range(len(strs)):
            l.append("".join(sorted(strs[i])))
        
        grp_words = defaultdict(list)
        
        for i in range(len(strs)):
            grp_words[l[i]].append(strs[i])
        
        res = []
        
        for k, v in grp_words.items():
            res.append(v)
            
        return res
        
        
