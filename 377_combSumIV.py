# 377. Combination Sum IV

# My memoized approach. For some reason exceeds time limit.

def recurse(nums, target, dp):
        
    if dp[target]!=0:
        return dp[target]
    
    if target==0:
        return dp[0]

    for n in nums:
        if n<=target:
            dp[target] += recurse(nums, target-n, dp)
            
    return dp[target]

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        dp = [0]*(target+1)
        dp[0] = 1
        
        # Bottom up Approach
        for i in range(1, target+1):
            for n in nums:
                if n<=target:
                    dp[i]+=dp[i-n]
                
        return dp[-1]
    
        # return recurse(nums, target, dp)
    

'''
# Someone else's memoized approach that doesnot exceed the time limit. The only difference being
# that he used a dictionary (memo) instead of a dp array.

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {}
        def dfs(nums, t, memo):
            if t in memo:
                return memo[t]
            if t == 0:
                return 1
            if t < 0:
                return 0
            res = 0
            for i in nums:
                res += dfs(nums, t-i, memo)
            memo[t] = res
            return res
        return (dfs(nums, target, memo))
'''
        
