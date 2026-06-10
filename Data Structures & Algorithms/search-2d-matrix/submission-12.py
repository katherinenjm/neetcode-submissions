class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #do binary search for each row and if reach final rown and no target found return false
        m = len(matrix)
        n = len(matrix[0]) -1

        #first we check whihc row the target is in

        i = 0
        target_row = -1
        while i < m :
            if target > matrix[i][n]:
                #target is not in row i, can discard
                i += 1
            elif target < matrix[i][n]:
                target_row = i
                i += m
            elif target == matrix[i][n]:
                return True
        if target_row == -1:
            return False
                
            



        #we now know what row were searching in: matrix[target_row]
        L = 0
        R = n



        #for a given row we implement binary search
        while L <= R:
            mid  = (L + R) // 2

            if target < matrix[target_row][mid]:
                R = mid -1
            elif target > matrix[target_row][mid]:
                L = mid + 1
            else:
                return True
        return False

        