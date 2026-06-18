class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        ROWS = len(obstacleGrid)
        COLS = len(obstacleGrid[0])
        if obstacleGrid[ROWS-1][COLS-1] == 1:
            return 0
        prev_row =[0] * COLS
        prev_row[COLS-1] = 1


        for i in range(ROWS-1, -1, -1):
            curr_row = [0] * COLS
            if obstacleGrid[i][COLS-1] != 1 and prev_row[COLS-1] == 1:
                curr_row[COLS-1] = 1
            for c in range(COLS-2, -1, -1):
                if obstacleGrid[i][c] == 1:
                    print(f"onbstacle found at obstacleGrid[{i}][{c}]")
                    curr_row[c] = 0
                else:
                    curr_row[c] = curr_row[c+1] + prev_row[c]
            print(f"for row = {i}, curr_Row = {curr_row}")
            print(f"for row = {i}, prev_row = {prev_row}")
            prev_row = curr_row
        return prev_row[0]

        