class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        rows = len(grid)
        cols = len(grid[0])
        seen = set()
        q = deque()

        def add_island(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or (r, c) in seen or grid[r][c] == -1:
                return 
            seen.add((r, c))
            q.append([r, c])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append([r, c])
                    seen.add((r, c))
        
        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()

                grid[r][c] = dist

                add_island(r + 1, c)
                add_island(r - 1, c)
                add_island(r, c + 1)
                add_island(r, c - 1)

            dist += 1