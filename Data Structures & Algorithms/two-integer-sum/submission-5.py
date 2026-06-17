class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        twosums_hashm = {}
        
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                twosums_hashm[nums[i]+nums[j]] = [i,j]


        return twosums_hashm[target]

        
        