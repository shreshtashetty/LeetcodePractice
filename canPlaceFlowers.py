# 605. Can Place Flowers

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed)==1:
            if n==0:
                return True
            if n>0 and flowerbed[0]==1:
                return False
            elif n==1 and flowerbed[0]==0:
                return True
            elif n>1:
                return False
        
        while(n>0):
            for i in range(len(flowerbed)):
                if i==0 and flowerbed[i]==0 and flowerbed[i+1]==0:
                    flowerbed[i]=1
                    n-=1
                elif i>0 and i<len(flowerbed)-1 and flowerbed[i]==0:
                    if flowerbed[i+1]==0 and flowerbed[i-1]==0:
                        flowerbed[i]=1
                        n-=1
                elif i==len(flowerbed)-1 and flowerbed[i-1]==0 and flowerbed[i]==0:
                    flowerbed[i]=1
                    n-=1
                if n==0:
                    return True
            if n!=0:
                return False
  
        return True
                    
        
