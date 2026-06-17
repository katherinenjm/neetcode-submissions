class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)
        # dict = {}
        # for num in nums:
        #     if num not in dict:
        #         dict[num] = 1
        #     else:
        #         return True
        # return False
                


        
        