# 80. Remove Duplicates from Sorted Array II

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        # A MORE ELEGANT SOLUTION: SLOWER THAN MINE THOUGH
        # i = 0
        # for n in nums:
        #     if i < 2 or n > nums[i-2]:
        #         nums[i] = n
        #         i += 1
        # return i
        
        # #MY REVISED BUT MORE ELEGANT SOLUTION (MORE OR LESS THE SAME AS ABOVE)
        i = 0
        for n in nums:
            if i<2:
                i+=1
                continue
            if i>=2 and n>nums[i-2]:
                nums[i] = n
                i+=1
        return i

# # MY HACKY BUT SUPER FAST SOLUTION
#         hash_map = {}
#         i=0
#         a = len(nums)
        
#         while i<a:
#             hash_map[nums[i]] = 1+hash_map.get(nums[i],0)
#             if hash_map[nums[i]]>2:
#                 nums.append(nums.pop(i))
#                 a-=1
#                 continue
#             i+=1
                
#         return i
                
            
