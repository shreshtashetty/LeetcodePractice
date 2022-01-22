# 93. Restore IP Addresses

def backtrack(s, arr, res):
    
    if len(arr)==4 and s=="":
        
        for j in range(len(arr)):
            if (arr[j][0]=="0" and len(arr[j])>1) or int(arr[j])>255:
                return
            
        if ".".join(arr) not in res:
            res.append(".".join(arr.copy()))
            
        return
    
    for i in range(len(s)):
        arr.append(s[:i+1])
        backtrack(s[i+1:],arr,res)
        arr.pop()
        
    return
        
    

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        backtrack(s, [], res)
        return res
