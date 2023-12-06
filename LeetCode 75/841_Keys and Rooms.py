class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)

        def dfs(u):
            visited[u] = 1
            for v in rooms[u]:
                if not visited[v]:
                    dfs(v)

        visited = [0] * n
        dfs(0)

        for i in range(n):
            if visited[i] == 0:
                return False
        return True
