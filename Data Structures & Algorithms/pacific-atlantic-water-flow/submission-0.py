class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        res = []

        def coast_to_coast(r, c, h):
            nonlocal atlantic
            nonlocal pacific
            if r < 0 or r >= rows or c < 0 or c >= cols or heights[r][c] > h or (r, c) in seen:
                return
            if r == 0 or c == 0:
                pacific = True
            if r == rows - 1 or c == cols - 1:
                atlantic = True

            directions = [
                [1, 0],
                [-1, 0],
                [0, 1],
                [0, -1]
            ]

            seen.add((r, c))

            for dr, dc in directions:
                coast_to_coast(r + dr, c + dc, heights[r][c])

        for r in range(rows):
            for c in range(cols):
                pacific = False
                atlantic = False
                seen = set()
                coast_to_coast(r, c, float("inf"))
                if pacific and atlantic:
                    res.append([r, c])

        return res