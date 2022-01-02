# 1143. Longest Common Subsequence

# # Recursion which takes 2^n time

# def solve(text1, text2, l):
    
#     if text1=='' or text2=='':
#         return l
    
#     if text1[0]==text2[0]:
#         l+=1
#         l = solve(text1[1:], text2[1:], l)
#     else:
#         l = max(solve(text1[1:], text2, l), solve(text1, text2[1:],l))
    
#     return l

# Memoization which takes mxn time.
def solve(text1, text2, dp, m, n):
    
    if m==0 or n==0:
        return 0
    
    if dp[m][n]!=-1:
        return dp[m][n]
    
    if text1[m-1]==text2[n-1]:
        dp[m][n] = 1+solve(text1[:m-1], text2[:n-1], dp, m-1, n-1)
    else:
        dp[m][n] = max(solve(text1[:m-1], text2, dp, m-1, n), solve(text1, text2[:n-1], dp, m, n-1))
    
    return dp[m][n]
    

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        dp=[[-1 for i in range(len(text2)+1)]for i in range(len(text1)+1)]
        
        l = solve(text1, text2, dp, len(text1), len(text2))
        return l
