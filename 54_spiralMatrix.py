# 54. Spiral Matrix

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        rmin, cmin = 0, 0
        rmax, cmax = len(matrix)-1, len(matrix[0])-1
        print(rmax, cmax)
        
        res = []
        
        while(cmin<=cmax and rmin<=rmax):
         
            for i in range(cmin, cmax+1):
                res.append(matrix[rmin][i])
                
            rmin+=1
            
            for i in range(rmin, rmax+1):
                res.append(matrix[i][cmax])
                
            cmax-=1
            
            if rmin<=rmax:
                for i in range(cmax, cmin-1, -1):
                    res.append(matrix[rmax][i])

                rmax-=1
            
            if cmin<=cmax:
                for i in range(rmax, rmin-1, -1):
                    res.append(matrix[i][cmin])

                cmin+=1
        
        return res
            
            
                
        
