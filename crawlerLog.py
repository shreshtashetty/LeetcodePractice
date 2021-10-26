# 1598. Crawler Log Folder

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        
        ops = 0
        
        for i in range(len(logs)):
            
            if logs[i][-3:] == "../":
                if ops==0:
                    continue
                else:
                    ops-=1
            elif logs[i][-2:] == "./":
                continue
            elif logs[i][-1] =="/":
                ops+=1
            
        return ops
