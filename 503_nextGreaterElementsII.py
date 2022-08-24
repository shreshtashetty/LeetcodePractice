# 503. Next Greater Element II

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        stack = []
        hash_map = {}
        
        for i, n in enumerate(nums):
            
            while stack and nums[stack[-1]]<n:
                ind = stack.pop()
                hash_map[ind] = i
            stack.append(i)
        
        for i in range(0, stack[0]+1):
            
            while stack and nums[stack[-1]]<nums[i]:
                ind = stack.pop()
                hash_map[ind] = i
            stack.append(i)
            
        
        ans = [-1]*len(nums)
        for k, v in hash_map.items():
            ans[k] = nums[v]
        
        return ans
