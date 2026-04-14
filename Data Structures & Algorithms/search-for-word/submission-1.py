class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row_size = len(board)
        col_size = len(board[0])
        
        def backtrack(i, r, c) -> bool:
            if i == len(word):
                return True
                
            if r >= row_size or r < 0 or c >= col_size or c < 0 or board[r][c] != word[i]:
                return False

            letter = board[r][c]
            board[r][c] = "*"

            found = (
                    backtrack(i + 1, r - 1, c) or 
                    backtrack(i + 1, r + 1, c) or
                    backtrack(i + 1, r, c - 1) or
                    backtrack(i + 1, r, c + 1)
            )

            board[r][c] = letter
            return found

        
        for row in range(row_size):
            for col in range(col_size):
                if backtrack(0, row, col):
                    return True

        return False