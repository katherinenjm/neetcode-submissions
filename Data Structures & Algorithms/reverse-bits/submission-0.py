class Solution:
    def reverseBits(self, n: int) -> int:
        counter = 31
        answer = 0
        while n:
            if n & 1:
                answer += 2**counter
            n = n >> 1
            counter -= 1
        return answer


             
        