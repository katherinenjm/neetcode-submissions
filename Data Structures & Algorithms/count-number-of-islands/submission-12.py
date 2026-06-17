class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        island_count = 0
        def dfs(row,col):
            if row < 0 or row ==ROWS or col < 0 or col == COLS or grid[row][col] == "0":
                return
            if grid[row][col] == "1":
                grid[row][col] = "0"
                

            dfs(row+1, col )
            dfs(row-1, col )
            dfs(row,   col+1 )
            dfs(row,   col-1 )

            return grid

        for r in range(ROWS):
            for c in range(COLS): 
                if grid[r][c] == "1":
                    print("island coast found")
                    island_count += 1
                    dfs(r,c)

        return island_count




        
        