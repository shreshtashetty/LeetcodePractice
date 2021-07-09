# 119. Pascal's Triangle II

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        l = []
        l.append([0,1,0])
        
        while(len(l)<rowIndex+1):
            l.append([0])
            for i in range(len(l[-2])-1):
                l[-1]+=[l[-2][i]+l[-2][i+1]]
            l[-1]+=[0]
        
        return l[-1][1:-1]
            
            
        
