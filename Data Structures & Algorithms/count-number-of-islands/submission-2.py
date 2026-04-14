class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        islands = 0
        rows = len(grid)
        cols = len(grid[0])
        seen = set()

        def dfs(r, c):
            if r >= 0 and r < rows and c >= 0 and c < cols and (r, c) not in seen and grid[r][c] == "1":
                directions = [[0, 1], [0, -1], [1, 0], [-1,0]]
                seen.add((r, c))
                for dr, dc in directions:
                    dfs(r + dr, c + dc)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in seen:
                    islands += 1
                    dfs(r, c)

        return islands
