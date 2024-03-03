class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adj = [[] for i in range(n)]
        visited = [0] * n

        for edge in edges:
            u, v = edge
            adj[u].append(v)
            adj[v].append(u)

        def dfs(u):
            visited[u] = 1
            time = 0

            for v in adj[u]:
                if not visited[v]:
                    childTime = dfs(v)
                    if childTime or hasApple[v]:
                        time += childTime + 2

            return time

        return dfs(0)
