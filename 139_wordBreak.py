# 139. Word Break

'''
# BRUTE FORCE APPROACH. CORRECT BUT EXCEEDS TIME LIMIT.
def recur(s, wordDict, all_combs, comb):
    
    if len(s)==0:
        # print(comb)
        all_combs.append(comb.copy())
        # print("HERE")
        return
    
    for j in range(len(s)):
        if s[:j+1] in wordDict:
            comb.append(s[:j+1])
            # print(comb)
            recur(s[j+1:], wordDict, all_combs, comb)
            comb.pop()
    
    return 
        
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        wordDict = set(wordDict)
        all_combs = []
        recur(s, wordDict, all_combs, comb=[])
        print(all_combs)
        return True if all_combs else False
'''
# https://www.youtube.com/watch?v=Sx9NNgInc3A

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        dp = [False]*(len(s)+1)
        dp[len(s)] = True
        
        for i in range(len(s)-1, -1, -1):
            for w in wordDict:
                if i+len(w)<=len(s) and s[i:i+len(w)]==w:
                    dp[i] = dp[i+len(w)]
                if dp[i]:
                    break

        return dp[0]
                
