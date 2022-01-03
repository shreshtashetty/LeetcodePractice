# 997. Find the Town Judge

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        if not trust and n>1:
            return -1
        
        hashmap = {} #finds the no of times a person trusts. (0 for the judge for the judge trusts nobody)
        for i in range(n):
            hashmap[i+1] = 0
        
        for i in range(len(trust)):
            hashmap[trust[i][0]]+=1
        
        hashmap1 = {} #finds the number times a person has been trusted. (n-1 for the judge for everyone                         
                      #trusts the judge except for the judge himself)
        for i in range(n):
            hashmap1[i+1] = 0
            
        for i in range(len(trust)):
            hashmap1[trust[i][1]]+=1
        
        for i in range(n):
            if hashmap[i+1]==0 and hashmap1[i+1]==n-1:
                return i+1
        return -1
