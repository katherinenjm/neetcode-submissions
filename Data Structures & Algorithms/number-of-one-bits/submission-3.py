class Solution:
    def hammingWeight(self, n: int) -> int:
        length = 0
        while n:
            length += 1 & n
            n = n >> 1
        return length

        