class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        seen = set()
        res = 0

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(node):
            for nei in adj[node]:
                if nei not in seen:
                    seen.add(nei)
                    dfs(nei)
        

        for node in range(n):
            if node not in seen:
                seen.add(node)
                dfs(node)
                res += 1

        return res