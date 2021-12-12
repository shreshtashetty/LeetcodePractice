# 416. Partition Equal Subset Sum

# Kevin Naughton Jr's Solution: https://www.youtube.com/watch?v=3N47yKRDed0
# Memoization with recursion.
# Simulate taking and not taking indices, memoize repeated operations.

def checkPartition(nums, index, sum_, total, state):
    
    curr_state = str(index) + " " + str(sum_)
    
    if curr_state in state:
        return state[curr_state]
    
    if sum_*2==total:
        return True
    
    if index >=len(nums) or sum_>total/2:
        return False
    
    foundPartition = checkPartition(nums, index+1, sum_, total, state) or \
checkPartition(nums, index+1, sum_+nums[index], total, state)
    
    state[curr_state] = foundPartition
    
    return foundPartition

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        if sum(nums)%2 != 0:
            return False
        
        return checkPartition(nums, 0, 0, sum(nums), {})
