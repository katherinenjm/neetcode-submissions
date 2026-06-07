class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        

        print(f"sorted_nums = {nums}, reverse_sorted_nums = {(nums[::-1])}, val = {val}")
        nums.sort()

    

        if val in nums:   
            first_inst_val =  nums.index(val)
            last_inst_val  = len(nums) - (nums[::-1]).index(val)

            print(f"values up to first_first_inst_val = {nums[:first_inst_val]}")
            print(f"values after last_inst_val = {nums[last_inst_val:]}")
            print(f"concat should look like this, nums = {nums[:first_inst_val] + nums[last_inst_val:]}")

        

            concat_nums = nums[:nums.index(val)] + nums[len(nums) - (nums[::-1]).index(val):]
            nums[:len(concat_nums)] = concat_nums
            
        
            return len(concat_nums) 
        else:
            return len(nums)      

        
        
        
        

        

        