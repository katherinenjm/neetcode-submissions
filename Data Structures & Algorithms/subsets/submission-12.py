class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        outp = []
        subset = []
        def dfs(index):
            if index >= len(nums):
                outp.append(subset.copy())
                return
            #include nums[i]
            subset.append(nums[index])
            dfs(index+1)

            #not inclue nums[i] 
            subset.pop()
            dfs(index+1)  

        dfs(0)
        return outp         
            
    

        