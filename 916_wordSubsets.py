# 916. Word Subsets

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        
        hash_w2s = {}
        res = []
        
        for w2 in words2:
            hash_w2 = {}
            for l in w2:
                hash_w2[l] = 1 + hash_w2.get(l, 0)
                hash_w2s[l] = max(hash_w2s.get(l,0), hash_w2[l]) # Get max count of each letter over all the words in words2 and compare that with the word counts in words1. That way you won't have to iterate over the words2 array each time you have to compare with words1.
                
        
        for w1 in words1:
            hash_w1 = {}
            for l in w1:
                hash_w1[l] = 1 + hash_w1.get(l, 0)
            # print(hash_w1)
            
            flag=0
            for l2 in hash_w2s.keys():
                if l2 not in hash_w1.keys():
                    flag=1
                    break
                else:
                    if hash_w1[l2]<hash_w2s[l2]:
                        flag=1
                        break
            if flag==0:
                res.append(w1)
                    
        return res
            
