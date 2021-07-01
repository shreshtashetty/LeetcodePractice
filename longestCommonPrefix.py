# 14. Longest Common Prefix

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==1:
            return strs[0]
        
        for i in range(len(strs)):
            if not strs[i]:
                return ""
            
        prefix = ""
        ind = 0
        l = []
        
        min_l = 1000
        
        for i in range(len(strs)):
            if len(strs[i])<min_l:
                min_l=len(strs[i])
         
        point = 0
        prefix = ""
        while point<min_l:
            for i in range(1, len(strs)):
                if strs[0][point]!=strs[i][point]:
                    return prefix
            prefix+=strs[0][point]
            point+=1
        return prefix
            
