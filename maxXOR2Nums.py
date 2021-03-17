# 421. Maximum XOR of Two Numbers in an Array

# Refer to https://www.youtube.com/watch?v=wSgrc98d2lI for solution with tries.
# Brute force solution correct but exceeds time limit.

class Trie:
    def __init__(self):
        self.children = {}
        
class Solution:
    def __init__(self):
        self.root = Trie()
    
    def insertBit(self, num):
        bit_num = bin(num)[2:].zfill(32)
        node = self.root
        for bit in bit_num:
            if bit not in node.children:
                node.children[bit] = Trie()
            node = node.children[bit]
    
    def find_max_xor(self, num):
        bit_num = bin(num)[2:].zfill(32)
        node = self.root
        max_xor = ''
        for bit in bit_num:
            if bit == '0':
                oppo_bit = '1'
            elif bit == '1':
                oppo_bit = '0'
            
            if oppo_bit in node.children:
                max_xor += oppo_bit
                node = node.children[oppo_bit]
            else:
                max_xor += bit
                node = node.children[bit]
        return int(max_xor, 2)^num
                
        
    def findMaximumXOR(self, nums: List[int]) -> int:
        for num in nums:
            self.insertBit(num)
        
        max_xor = 0
        for num in nums:
            max_xor = max(max_xor, self.find_max_xor(num))
        
        return max_xor
        
# class Solution:
#     def findMaximumXOR(self, nums: List[int]) -> int:
#         max_xor = 0
        
#         # [3,10,5,25,2,8]
        
#         for i in range(len(nums)-1):
#             for j in range(i+1, len(nums)):
#                 xor = nums[i]^nums[j]
#                 if(xor>max_xor):
#                     max_xor = xor
#         return max_xor
        
