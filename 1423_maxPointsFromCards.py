# 1423. Maximum Points You Can Obtain from Cards

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        
        max_sum, sum_ = sum(cardPoints[0:k]),sum(cardPoints[0:k])
        
        last_ind = k-1
        new_ind = len(cardPoints)-1
        
        while k>0:
            
            sum_ = sum_-cardPoints[last_ind]+cardPoints[new_ind]
            max_sum = max(max_sum, sum_)
            last_ind-=1
            new_ind-=1
            k-=1
            
        return max_sum
        
        # # My old approach. Gives correct answer but gives TLE
        # cardPoints = cardPoints[-k:] + cardPoints
        # max_sum = 0
        # i = 0
        # while i<=k:
        #     max_sum = max(max_sum, sum(cardPoints[i:i+k]))
        #     i+=1
        # return max_sum
