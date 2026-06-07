class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        print(nums)
        outp = False
        for i in range(1,len(nums),1):
            if nums[i]==nums[i-1]:
                outp = True
                break
        return outp
                


        
        