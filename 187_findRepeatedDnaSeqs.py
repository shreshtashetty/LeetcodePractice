# 187. Repeated DNA Sequences

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        
        seqs = []
        
        hashset = {}
        maxlen = 0
        
        for i in range(0,len(s)-9):
            v = s[i:i+10]
            hashset[v] = 1+hashset.get(v,0)
            maxlen = max(maxlen,hashset[v])
        
        if maxlen<=1:
            return seqs
        
        for key,value in hashset.items():
            if value==maxlen:
                seqs.append(key)
        
        return seqs
            
        
        
