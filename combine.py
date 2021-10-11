# 77. Combinations

# NOT THE GREATEST SOLUTION. TRY COMING UP WITH SOMETHING BETTER.

class Solution:
    
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        arr = list(range(1, n+2)) # VERY HACKY
        coms = []
        visited = []
        self.combinations(arr, coms, visited, k, [])
        return coms
   

    def combinations(self, arr, coms, visited, k, new_com):
        
        # print(coms)
        
        for i in range(len(arr)):
            # print(arr[i])
            
            if len(new_com)<k:
                new_com.append(arr[i])
                self.combinations(arr[i+1:], coms, visited, k, new_com)
            
            if len(new_com)==k:
                # print(new_com)
                sorted_new_com = sorted(new_com)
                if sorted_new_com not in visited:
                    visited.append(sorted_new_com)
                    coms.append(sorted_new_com)
                new_com.pop()
                return
            
        if new_com:
            new_com.pop()
        return
        
        
