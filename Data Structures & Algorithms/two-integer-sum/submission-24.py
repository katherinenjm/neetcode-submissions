class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        twosums_hashm = {}

        # print(enumerate(nums))
        
        for i,n in enumerate(nums):
            print(f" i = {i}, n = {n}")
            twosums_hashm[n] = i
        print(twosums_hashm)

        for i,n in enumerate(nums):
            second_index = target - n
            if second_index in twosums_hashm and twosums_hashm[second_index] != i:
                return [i, twosums_hashm[second_index]]
        
        