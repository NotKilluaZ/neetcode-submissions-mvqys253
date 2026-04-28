class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)
        for u, v, t in times:
            edges[u].append((v, t))

        min_heap = [(0, k)]
        seen = set()
        t = 0
        while min_heap:
            t1, n1 = heapq.heappop(min_heap)
            if n1 in seen:
                continue
            seen.add(n1)
            t = t1

            for n2, t2 in edges[n1]:
                if n2 not in seen:
                    heapq.heappush(min_heap, (t1 + t2, n2))
        
        return t if len(seen) == n else -1