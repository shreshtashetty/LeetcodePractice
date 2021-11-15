# 292. Nim Game

class Solution:
    def canWinNim(self, n: int) -> bool:
        """
        You can always win a Nim game if the number of stones 
        n in the pile is not divisible by 4.
        """
        return (n % 4 != 0)
        
