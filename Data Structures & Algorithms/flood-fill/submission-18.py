class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROWS = len(image)
        COLS = len(image[0])
        starting_col = image[sr][sc]
        self.color = color
        if starting_col == self.color:
            return image
        def dfs(image,r,c):
            if r < 0 or c < 0 or r == ROWS or c == COLS or image[r][c] != starting_col:
                return image

            image[r][c] = self.color
            
            dfs(image, r+1, c  )
            dfs(image, r-1, c  )
            dfs(image, r,   c+1)
            dfs(image, r,   c-1)

            return image
        return dfs(image, sr, sc)

    
        

        
        

