# 165. Compare Version Numbers

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split('.')
        v2 = version2.split('.')
        
        l = min(len(v1), len(v2))
        
        for i in range(l):
            i1 = int(v1[i])
            i2 = int(v2[i])
            if i1<i2:
                return -1
            elif i2<i1:
                return 1
            
        if len(v1)>len(v2):
            rem = v1[i+1:]
            for i in range(len(rem)):
                if int(rem[i])>0:
                    return 1
            return 0
                
        elif len(v2)>len(v1):
            rem = v2[i+1:]
            for i in range(len(rem)):
                if int(rem[i])>0:
                    return -1
            return 0
                
        return 0
        
        
