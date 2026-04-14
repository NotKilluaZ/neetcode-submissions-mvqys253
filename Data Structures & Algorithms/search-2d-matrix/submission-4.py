class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1
        row = []
        while l <= r:
            m = ((r - l) // 2) + l
            if matrix[m][-1] < target:
                l = m + 1
            elif matrix[m][0] > target:
                r = m - 1
            else:
                row = matrix[m]
                break

        l = 0
        r = len(row) - 1
        while l <= r:
            m = ((r - l) // 2) + l
            if row[m] == target:
                return True
            elif row[m] < target:
                l = m + 1
            else:
                r = m - 1

        return False