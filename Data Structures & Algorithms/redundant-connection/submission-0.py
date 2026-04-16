class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(len(edges) + 1)]

        def dfs(node, par):
            if node in seen:
                return True

            seen.add(node)

            for nei in adj[node]:
                if nei == par:
                    continue
                if dfs(nei, node):
                    return True

            return False

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            seen = set()
            if dfs(u, -1):
                return [u, v]

        return []