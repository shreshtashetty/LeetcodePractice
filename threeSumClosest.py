# 16. 3Sum Closest

# Nick White's Soln: https://www.youtube.com/watch?v=qBr2hq4daWE

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        result = nums[0] + nums[1] + nums[-1]
        
        for i in range(len(nums)-2):
            a_pointer = i + 1
            b_pointer = len(nums)-1
            
            while(a_pointer<b_pointer):
                current = nums[i] + nums[a_pointer] + nums[b_pointer]
                if current>target:
                    b_pointer-=1
                else:
                    a_pointer+=1
                
                if abs(current-target)<abs(result-target):
                    result = current
        return result
