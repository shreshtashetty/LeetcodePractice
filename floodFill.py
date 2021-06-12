# 733. Flood Fill

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        if image[sr][sc] == newColor:
            return image
        
        orig_color = image[sr][sc]
        image[sr][sc] = newColor
        
        if sr+1<len(image) and image[sr+1][sc] == orig_color:
            image = self.floodFill(image, sr+1, sc, newColor)
            
        if  sr-1>=0 and image[sr-1][sc] == orig_color:
            image = self.floodFill(image, sr-1, sc, newColor)
            
        if sc+1<len(image[0]) and image[sr][sc+1] == orig_color:
            image = self.floodFill(image, sr, sc+1, newColor)
            
        if sc-1>=0 and image[sr][sc-1] == orig_color:
            image = self.floodFill(image, sr, sc-1, newColor)
            
        return image
            
        
                
                
