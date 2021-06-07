# 771. Jewels and Stones

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels = list(jewels)
        stones = list(stones)
        
        count = 0
        for i in range(len(stones)):
            if stones[i] in jewels:
                count+=1
        return count
                
        
