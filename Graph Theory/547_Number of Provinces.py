class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(u):
            visited[u] = 1
            for v in range(len(isConnected)):
                if isConnected[u][v] == 1 and not visited[v]:
                    dfs(v)

        n = len(isConnected[0])
        #visited = [[0 for j in range(n)]for i in range(n)]
        visited = [0] * n
        cnt = 0
        for i in range(n):
            if visited[i] == 0:
                cnt += 1
                dfs(i)
        return cnt
