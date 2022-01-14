# 904. Fruit Into Baskets

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        if len(fruits)<3:
            return len(fruits)
        
        fruit_set = set()
        maxl = 0
        arr= []
        
        for i in range(len(fruits)):
            
            if fruits[i] not in fruit_set and len(fruit_set)<2:
                
                fruit_set.add(fruits[i])
                arr.append(fruits[i])
                
            elif fruits[i] not in fruit_set and len(fruit_set)==2:
            
                temp = arr[-1]
                for j in range(len(arr)-1, -1, -1):
                    if arr[j]!=temp:
                        break
                        
                arr = arr[j+1:]+[fruits[i]]
                fruit_set = set(arr)
        
                
            elif fruits[i] in fruit_set:
                
                arr.append(fruits[i])
                
            maxl = max(maxl,len(arr))

        return maxl
