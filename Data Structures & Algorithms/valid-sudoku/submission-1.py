class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            seen = set()
            for i in range(9):
                if row[i] in seen:
                    return False
                if row[i] != ".":
                    seen.add(row[i])
        
        for col in range(9):
            seen = set()
            for row in board:
                if row[col] in seen:
                    return False
                if row[col] != ".":
                    seen.add(row[col])

        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                seen = set()
                for r in range(row, row + 3):
                    for c in range(col, col + 3):
                        if board[r][c] in seen:
                            return False
                        if board[r][c] != ".":
                            seen.add(board[r][c])

        return True        