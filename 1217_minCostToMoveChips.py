# 1217. Minimum Cost to Move Chips to The Same Position

# Brainteaser. All chips at even positions can be moved to 0 at 0 cost and the same can be 
# done for the chips at odd positions. It makes more sense then to move the pile with the 
# lowest number of chips on to the other with cost = 1. Therefore just count number of chips at 
# odd positions and no of chips at even positions and return the min.

class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:

        even_cnts, odd_cnts = 0, 0
        
        for i in range(len(position)):

            if position[i]%2==1:
                odd_cnts+=1
            else:
                even_cnts+=1
                
        return min(odd_cnts, even_cnts)
