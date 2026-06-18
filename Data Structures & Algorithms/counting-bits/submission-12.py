class Solution:
    def countBits(self, n: int) -> List[int]:
        hamming_weights = [0] * (n+1)
        if n == 0:
            return hamming_weights
        
        for i in range(1, n+1 ):
            if (i ^ i-1) == 0:
                hamming_weights[i] = 1
            if (i ^ i+1) == 0:
                hamming_weights[i] = i-1
            dummy_i = i
            weight = 0
            while dummy_i:
                dummy_i = (dummy_i & (dummy_i -1))
                hamming_weights[i] += 1

        return hamming_weights

        