class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        min_heap = [[grid[0][0], 0, 0]]
        seen = set()
        seen.add((0, 0))
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        while min_heap:
            t, r, c = heapq.heappop(min_heap)
            seen.add((r, c))

            if r == N - 1 and c == N - 1:
                return t

            for dr, dc in directions:
                nei_r, nei_c = r + dr, c + dc
                if nei_r < 0 or nei_c < 0 or nei_r >= N or nei_c >= N or (nei_r, nei_c) in seen:
                    continue
                
                seen.add((nei_r, nei_c))
                heapq.heappush(min_heap, [max(t, grid[nei_r][nei_c]), nei_r, nei_c])
            