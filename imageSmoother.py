# 661. Image Smoother

import numpy as np

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m,n = len(img), len(img[0])
        
        img = np.array(img)
        img_cpy = np.zeros((m,n))
        
        def isValid(i,j):
            if i>=0 and i<m and j>=0 and j<n:
                return True
            else:
                return False
            
        for i in range(m):
            for j in range(n):
                val = 0
                cnt = 0
                for x in range(-1,2):
                    for y in range(-1,2):
                        if isValid(i+x,j+y):
                            val+=img[i+x,j+y]
                            cnt+=1
                img_cpy[i,j] = val//cnt
                

        return img_cpy.astype(int)
        
