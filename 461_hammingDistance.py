# 461. Hamming Distance

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # Refer to their solutions
        # x^y does binary xor and returns the number got after doing the xor
        # doing bin(x^y) gives the binary value to the xor.
        xor = bin(x^y)
        return xor.count('1')
