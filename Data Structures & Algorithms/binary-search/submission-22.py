class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #implement binary sort
        L = 0
        R = len(nums)-1

        while L <= R:
            mid = (L + R) //2
            print(f" L = {L}, R= {R}, mid = {mid}")


            if target > nums[mid]:
                print(f" for mid = {mid},  (target = {target}) > (nums[mid] = {nums[mid]})")
                L = mid + 1
            elif target < nums[mid]:
                print(f" for mid = {mid},  (target = {target}) < (nums[mid] = {nums[mid]})")
                R = mid - 1
            else:
                return mid

        return -1


        