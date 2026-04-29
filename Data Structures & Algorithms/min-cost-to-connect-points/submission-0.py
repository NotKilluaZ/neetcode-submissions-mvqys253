class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = {i : [] for i in range(len(points))}

        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i + 1, len(points)):
                x2, y2 = points[j]
                manhatten_dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([manhatten_dist, j])
                adj[j].append([manhatten_dist, i])

        min_heap = [[0, 0]]
        seen = set()
        res = 0

        while len(seen) < len(points):
            cost, i = heapq.heappop(min_heap)
            if i in seen:
                continue
            res += cost
            seen.add(i)

            for nei_cost, nei in adj[i]:
                heapq.heappush(min_heap, [nei_cost, nei])

        return res