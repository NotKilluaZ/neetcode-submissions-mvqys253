class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        seen = set()
        area = 0

        def dfs(r, c):
            area = 0
            if r >= 0 and r < rows and c >= 0 and c < cols and grid[r][c] == 1 and (r, c) not in seen:
                directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                seen.add((r, c))
                area = 1
                for dr, dc in directions:
                    area += dfs(r + dr, c + dc)
            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in seen:
                    cand_area = dfs(r, c)
                    area = max(area, cand_area)

        return area

        