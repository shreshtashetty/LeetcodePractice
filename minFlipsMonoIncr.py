# 926. Flip String to Monotone Increasing

# Weird solution by Leetcode

class Solution:
    def minFlipsMonoIncr(self, S: str) -> int:
        P = [0]
        for x in S:
            P.append(P[-1]+int(x))

        all_ans = []
    
        for i in range(len(P)):
            all_ans.append(P[i] + (len(S)-i)-(P[-1]-P[i]))

        return min(all_ans)
        
