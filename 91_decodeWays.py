# 91. Decode Ways

# Kevin Naughton Jr: https://www.youtube.com/watch?v=cQX3yHS0cLo

# https://leetcode.com/problems/decode-ways/discuss/253018/Python%3A-Easy-to-understand-explanation-bottom-up-dynamic-programming

class Solution:
    def numDecodings(self, s: str) -> int:
        
        if s[0]==0:
            return 0
        
        dp = [0]*(len(s)+1)
        dp[0] = 1
        
        if s[0]!='0':
            dp[1] = 1
        
        for i in range(2, len(s)+1):

            oneDigit = int(s[i-1])
            twoDigits = int(s[i-2:i])
  
            if oneDigit>0:
                dp[i] += dp[i-1]
            if 10<=twoDigits<=26:
                dp[i] += dp[i-2]
     
        return dp[-1]
            
    
