class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if row[-1] < target:
                continue
            for i in range(len(row)):
                if row[i] == target:
                    return True

        return False