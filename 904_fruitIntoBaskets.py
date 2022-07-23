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

# Another Solution
# 904. Fruit Into Baskets

# Problem boils down to longest substring with at most 2 characters.
# Kevin Naughton Jr's Solution: https://www.youtube.com/watch?v=za2YuucS0tw&t=341s
'''
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        if not fruits or len(fruits)==0:
            return 0
        
        max_len = 1
        
        i, j = 0, 0
        
        char_map = {}
        
        while(j<len(fruits)):
            
            if len(char_map)<=2:
                char_map[fruits[j]] = j
                
            if len(char_map)>2:
                min_ind = len(fruits)
                for vals in char_map.values():
                    min_ind = min(vals, min_ind)
                i = min_ind + 1
                del char_map[fruits[min_ind]]
                
            max_len = max(max_len, j-i+1)
            
            j+=1
            
        return max_len
 '''           
        
