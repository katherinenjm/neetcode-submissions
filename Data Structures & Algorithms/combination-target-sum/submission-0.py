class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        outp = []
        
        def dfs(i, curr, total):
            #basecase- success
            if total == target:
                outp.append(curr.copy())
                return
            #basecase-fail
            if total > target or i >= len(nums):
                return

            curr.append(nums[i])
            dfs(i,curr,total + nums[i])     #include vlaue
            curr.pop()
            dfs(i+1,curr, total)

        dfs(0, [], 0)

        return outp


            



