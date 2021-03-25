# 881. Boats to Save People

# Use two pointer method.

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        if len(people)==1:
            return 1
        
        people = sorted(people)
        
        pointer1 = 0
        pointer2 = len(people)-1
        
        num_boats = 0
        
        while(pointer1<=pointer2):
            if pointer1==pointer2:
                num_boats+=1
                pointer1+=1
                pointer2-=1
            else:
                if people[pointer2]+people[pointer1]>limit:
                    num_boats+=1
                    pointer2-=1
                elif people[pointer2] + people[pointer1]<=limit:
                    num_boats+=1
                    pointer2-=1
                    pointer1+=1
                
        return num_boats
        
