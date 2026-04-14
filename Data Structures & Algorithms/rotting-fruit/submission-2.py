class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1
        rows = len(grid)
        cols = len(grid[0])
        seen = set()
        q = deque()
        fresh = 0

        def add_cell(r, c):
            nonlocal fresh
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0 or grid[r][c] == 2 or (r, c) in seen:
                return 
            q.append([r, c])
            seen.add((r, c)) 
            fresh -= 1

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    seen.add((r, c))
                    q.append([r, c])
                elif grid[r][c] == 1:
                    fresh += 1

        time = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()

                grid[r][c] = 2

                add_cell(r + 1, c)
                add_cell(r - 1, c)
                add_cell(r, c + 1)
                add_cell(r, c - 1)

            time += 1

        return max(time - 1, 0) if fresh == 0 else -1