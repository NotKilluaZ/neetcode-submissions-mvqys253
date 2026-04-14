class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row_size = len(board)
        col_size = len(board[0])
        
        def backtrack(w, r, c) -> bool:
            if w == word:
                return True
                
            if r >= row_size or r < 0 or c >= col_size or c < 0 or board[r][c] == "*":
                return False

            letter = board[r][c]
            board[r][c] = "*"
            w += letter

            found = (
                    backtrack(w, r - 1, c) or 
                    backtrack(w, r + 1, c) or
                    backtrack(w, r, c - 1) or
                    backtrack(w, r, c + 1)
            )

            board[r][c] = letter
            return found

        
        for row in range(row_size):
            for col in range(col_size):
                if backtrack("", row, col):
                    return True

        return False