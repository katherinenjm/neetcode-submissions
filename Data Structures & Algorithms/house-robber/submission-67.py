class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def tabulation_dp(nums):
            if nums == []:
                return 0
            if len(nums) == 1:
                return nums[0]
            if len(nums) == 2:
                return max(nums[0], nums[1])
            dp = [nums[len(nums)-2], nums[len(nums)-1]]
            print(f"len(nums) = {len(nums)}")
            print(f"nums[len(nums)-1")
            print(f"dp = {dp}")
            i = len(nums)-3
            while i >=0:
                print(f"for i = {i},nums[i] = {nums[i]}, dp = {dp}")
                temp =dp[0]
                dp[0] = max((nums[i]+dp[1]), temp)
                dp[1] = temp
                i -= 1
                print(f"for i = {i},nums[i] = {nums[i]}, dp = {dp}")
            return dp[0]
        return tabulation_dp(nums)



            
            






        # # print(f"len(nums) -2 = {len(nums)-2}")
        # def rob_sum(i,cache):
        #     # print(f" i ={i}")
        #     cache[len(nums)-1] = nums[len(nums)-1]
        #     cache[len(nums)-2] = nums[len(nums)-2]
            
        #     if i >= len(nums) -2:
        #         return nums[i]
        #     if i in cache:
        #         return cache[i]
            
            
        #     cache[i]   = rob_sum(i+2,cache) + nums[i]
        #     # cache[i+1] = rob_sum(i+3,cache) + nums[i+1]
        #     print(f"for i = {i}, cache = {cache}")
        #     return max(cache[i], cache[i+1])
            
         
        # working_cache = [0]* len(nums) 
        # return rob_sum(0,working_cache)  