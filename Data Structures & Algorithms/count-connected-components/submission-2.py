class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(node, par):
            if node in seen:
                return
            seen.add(node)
            for nei in adj[node]:
                if nei in seen:
                    continue
                dfs(nei, node)

        res = 0
        seen = set()
        for node in range(n):
            if node in seen:
                continue
            dfs(node, -1)
            res += 1

        return res
            