class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        COLS = len(text1)
        ROWS = len(text2)
        prev_row = [0] * (COLS + 1)

        for r in range(ROWS-1,-1,-1):
            curr_row = [0] * (COLS+1)
            for c in range(COLS-1,-1,-1):
                if text1[c] == text2[r]:
                    curr_row[c] = 1 + prev_row[c+1]
                else:
                    curr_row[c] = max(curr_row[c+1], prev_row[c])
            prev_row = curr_row
        return prev_row[0]