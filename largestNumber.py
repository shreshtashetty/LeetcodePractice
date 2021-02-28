#GO THROUGH THEIR SOLUTION
class LargerNumKey(str): #inherits from string class
    def __lt__(x, y): # overloads behavior of __lt__ method which controls behavior of >
        return x+y > y+x
    
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(x) for x in nums]
        largest_num = ''.join(sorted(nums, key=LargerNumKey))
        if largest_num[0]=='0':
            return '0'
        else:
            return largest_num
