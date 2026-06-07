class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones   = 0
        ones_count = 0
        print(nums)
        for i in range(len(nums)):
            if nums[i]==1:
                ones_count += 1

            else:
                ones_count = 0
            print(f" for i = {i}, ones_count = {ones_count}")
            max_ones = max(max_ones, ones_count)
        return max_ones

            