class Solution:
    def checkPartitioning(self, s: str) -> bool:
        #least recently used cache. Allows function calls to be memoized, so that future
        #function calls with the same parameters can be returned instantly without having
        #to be recomputed
        @lru_cache(None) #None means boundless size of cache
        def pal(i, j):
            if(i==j):
                return True
            if(s[i]!=s[j]):
                return False
            if(i+1==j):
                return True
            else:
                return pal(i+1, j-1)
        # print(pal(0, 8))
        
        s_len = len(s)
        
        
        for i in range(s_len-2):
            if pal(0, i):
                for j in range(i+1, s_len-1):
                    if(pal(i+1, j) and pal(j+1, s_len-1)):
                        return True
        return False
