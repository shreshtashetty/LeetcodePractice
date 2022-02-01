# 1222. Queens That Can Attack the King

class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        
        i = king[0]
        j = king[1]
        
        res = []
        
        while i<8:
            if [i,j] in queens:
                res.append([i,j])
                break
            i+=1
        i = king[0]

        
        while i>=0:
            if [i,j] in queens:
                res.append([i,j])
                break
            i-=1
        i = king[0]
  
        while j<8:
            if [i,j] in queens:
                res.append([i,j])
                break
            j+=1
        j = king[1]

        
        while j>=0:
            if [i,j] in queens:
                res.append([i,j])
                break
            j-=1
        j = king[1]
            
        while i<8 and j<8:
            if [i,j] in queens:
                res.append([i,j])
                break
            i+=1
            j+=1
        
        i = king[0]
        j = king[1]
        
        while i>=0 and j>=0:
            if [i,j] in queens:
                res.append([i,j])
                break
            i-=1
            j-=1
        
        i = king[0]
        j = king[1]
        
        while i>=0 and j<8:
            if [i,j] in queens:
                res.append([i,j])
                break
            i-=1
            j+=1
        
        i = king[0]
        j = king[1]
        
        while i<8 and j>=0:
            if [i,j] in queens:
                res.append([i,j])
                break
            i+=1
            j-=1
        
        i = king[0]
        j = king[1]
            
        return res
            
        
        
