# 1306. Jump Game III

# Anish Malla's Solution: https://www.youtube.com/watch?v=GLTskY7KehU

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        
        q = collections.deque([])
        q.append(start)
        cache = set()
        
        while q:
            
            indx = q.popleft()
            if arr[indx]==0:
                return True
            
            for x in ((indx+arr[indx]),(ind-arr[indx])):
                
                if x>=0 and x<len(arr) and x not in cache:
                    q.append(x)
                    cache.add(indx)
        return False
