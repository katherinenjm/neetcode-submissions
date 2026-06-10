class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        colours = [0] * 3

        #count the number of each colour:
        for i in range(len(nums)):
            colours[nums[i]] += 1

        print(f"colours = {colours}")
        
        #repopulate the original with the values form the bucket
        index_nums = 0
        for index_colours_size in range(len(colours)):
            for index_colours_val in range(colours[index_colours_size]):
                print(f"index_colour_size = {index_colours_size}, index_colour_val = {index_colours_val}")
                print(f"for this round of the iteration, im writing value {index_colours_size} into index {index_nums} of the nums arr")
                nums[index_nums] = index_colours_size
                index_nums += 1