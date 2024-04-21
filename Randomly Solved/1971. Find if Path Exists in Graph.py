class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        def dfs(u):
            visited[u] = 1

            for v in adj_lst[u]:
                if not visited[v]:
                    dfs(v)

        visited = [0] * n
        adj_lst = [[] for i in range(n)]

        for u, v in edges:
            adj_lst[u].append(v)
            adj_lst[v].append(u)

        dfs(source)

        return visited[destination]
