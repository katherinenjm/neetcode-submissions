class Solution:
    def climbStairs(self, n: int) -> int:
        # #brute force recursive
        # if n == 1 or n==2:
        #     return n

        # return self.climbStairs(n-1) + self.climbStairs(n-2)

        # #memoisation
        # def memoisation(n,cache):
        #     if n <=2:
        #         return n
        #     if n in cache:
        #         return cache[n]
        #     # print(f"for n = {n}, cache = {cache}")
        #     cache[n] = memoisation(n-1, cache) + memoisation(n-2, cache)
        #     return cache[n]

        # working_cache = [0]*(n+1)

        # return memoisation(n, working_cache)
        
        #tabulation
        def dp(n):
            if n <=2:
                return n
            dp = [1,2]
            i = 3 #try maybe 3?
            while i <= n:
                temp = dp[1]
                dp[1] = dp[0] + temp
                dp[0] = temp
                i += 1
            return dp[1]
        return dp(n)
        
        
       
    