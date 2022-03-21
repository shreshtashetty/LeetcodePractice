# 763. Partition Labels

#Better Solution
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        last = {c:i for i,c in enumerate(s)}
        start = end = 0
        lengths = []
            
        for i, c in enumerate(s):
            end = max(end, last[c])
            
            if i==end:
                lengths.append(end-start+1)
                start = i+1
                
        return lengths
                
'''
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        end_in = 0
        start=0
        lengths = []
        for i in range(len(s)):
            for j in range(len(s)-1, i, -1):
                if s[i]==s[j] and j>end_in:
                    end_in = j
            if i==end_in:
                l = len(s[start:end_in+1])
                lengths.append(l)
                start = end_in+1
                end_in+=1
        return lengths
'''
