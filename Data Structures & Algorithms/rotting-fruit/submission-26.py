class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        
        queue = deque()
        fresh = 0
        minute = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r,c))
                elif grid[r][c] == 1:
                    fresh +=1
        
        while queue and fresh > 0:
            for i in range(len(queue)):
                r,c = queue.popleft()
                neighbours = [[0,1], [1,0], [0,-1], [-1,0]]
                for dr,dc in neighbours:
                    nr,nc = r+dr, c+dc
                    if  0 <= nr <ROWS and 0<= nc < COLS and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        queue.append((nr,nc))
                        fresh -= 1
            print(grid)
            print(fresh)
            minute += 1
        
        return minute if fresh ==0 else -1
        
                