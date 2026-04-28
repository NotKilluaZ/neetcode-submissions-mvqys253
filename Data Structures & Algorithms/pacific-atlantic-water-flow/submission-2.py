class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        rows = len(heights)
        cols = len(heights[0])
        pacific = set()
        atlantic = set()

        def dfs(r, c, h, seen):
            if r < 0  or r >= rows or c < 0 or c >= cols or h > heights[r][c] or (r, c) in seen:
                return

            seen.add((r, c))
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in directions:
                dfs(r + dr, c + dc, heights[r][c], seen)

        for r in range(rows):
            dfs(r, 0, heights[r][0], pacific)
            dfs(r, cols - 1, heights[r][cols - 1], atlantic)

        for c in range(cols):
            dfs(0, c, heights[0][c], pacific)
            dfs(rows - 1, c, heights[rows - 1][c], atlantic)

        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacific and (r, c)  in atlantic:
                    res.append([r, c])

        return res