class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0  #index for nums1 comparison to nums2
        j = 0  #index for nums2 comparison to nums1
        k = 0  #index for writing value to nums1

        #we only need a temproary variable for nums1 as nums2 isnt being written to!
        temp1 = nums1[:m]

        
        while i < m and j < n :
            print(f"i = {i}, j = {j}, k = {k}")
            
            if temp1[i]<= nums2[j]:
                nums1[k] = temp1[i]
                i += 1
                k += 1
            else:
                nums1[k] = nums2[j]
                j += 1
                k += 1
        
        while j < n :
            print(f"i = {i}, j = {j}, k = {k}")
            nums1[k] = nums2[j]
            j += 1
            k += 1

        while i < m :
            print(f"i = {i}, j = {j}, k = {k}")
            print(f"im trying to print temp1[{i}] = {temp1[i]} to index {k} of nums1")
            nums1[k] = temp1[i]
            i += 1
            k += 1




