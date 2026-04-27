class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        
        def backtrack(r, c, i):
            if i == len(word):
                return True

            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[i]:
                return False

            letter = board[r][c]
            board[r][c] = "*"

            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            found = False
            for dr, dc in directions:
                found = found or backtrack(r + dr, c + dc, i + 1)

            board[r][c] = letter
            return found

        for r in range(rows):
            for c in range(cols):
                if backtrack(r, c, 0):
                    return True

        return False