class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        from queue import Queue

        def bfs(x, y):
            visited[x][y] = 1
            q = Queue()
            q.put((x, y))

            while not q.empty():
                u, v = q.get()

                if [u, v] != entrance and maze[u][v] == '.' and (u in [0, len(maze)-1] or v in [0, len(maze[0])-1]):
                    return [u, v]

                # up
                if u > 0 and maze[u-1][v] == '.' and not visited[u-1][v]:
                    q.put((u-1, v))
                    visited[u-1][v] = 1
                    parent[(u-1, v)] = (u, v)

                # down
                if u < len(maze)-1 and maze[u+1][v] == '.' and not visited[u+1][v]:
                    q.put((u+1, v))
                    visited[u+1][v] = 1
                    parent[(u+1, v)] = (u, v)

                # left
                if v > 0 and maze[u][v-1] == '.' and not visited[u][v-1]:
                    q.put((u, v-1))
                    visited[u][v-1] = 1
                    parent[(u, v-1)] = (u, v)

                # right
                if v < len(maze[0])-1 and maze[u][v+1] == '.' and not visited[u][v+1]:
                    q.put((u, v+1))
                    visited[u][v+1] = 1
                    parent[(u, v+1)] = (u, v)

            return -1


        visited = [[0 for i in range(len(maze[0]))] for i in range(len(maze))]
        parent = dict()

        ret = bfs(entrance[0], entrance[1])

        if ret == -1:
            return ret
        
        u, v = ret
        ans = 0
        while [u, v] != entrance:
            ans += 1
            u, v = parent[(u, v)]

        return ans
