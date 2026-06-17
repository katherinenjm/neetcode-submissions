class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [[1,0], [-1,0], [0,1],[0,-1]]
        max_area = 0


        def dfs(row,col,island_area):
            
            if row < 0 or row == ROWS or col < 0 or col == COLS or grid[row][col] == 0:
                return 0
            
            
            grid[row][col] = 0
            island_area = 1

            for dir_row, dir_col in directions:
                island_area += dfs(row + dir_row, col + dir_col,island_area)
            return island_area

        
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    # print(dfs(row,col,0))
                    max_area = max(max_area,dfs(row,col,0))
                    

        return max_area
        