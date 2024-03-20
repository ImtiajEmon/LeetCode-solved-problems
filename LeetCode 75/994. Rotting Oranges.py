class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from queue import Queue

        def bfs():
            nonlocal time, fresh

            while not q.empty():
                time += 1

                for i in range(q.qsize()):
                    u, v = q.get()

                    # up
                    if u > 0 and grid[u-1][v] != 0 and not visited[u-1][v]:
                        q.put((u-1, v))
                        visited[u-1][v] = 1
                        fresh -=  1

                    # down
                    if u < len(grid)-1 and grid[u+1][v] != 0 and not visited[u+1][v]:
                        q.put((u+1, v))
                        visited[u+1][v] = 1
                        fresh -=  1

                    # left
                    if v > 0 and grid[u][v-1] != 0 and not visited[u][v-1]:
                        q.put((u, v-1))
                        visited[u][v-1] = 1
                        fresh -=  1

                    # right
                    if v < len(grid[0])-1 and grid[u][v+1] != 0 and not visited[u][v+1]:
                        q.put((u, v+1))
                        visited[u][v+1] = 1
                        fresh -=  1


        rows, cols = len(grid), len(grid[0])
        visited = [[0 for i in range(cols)] for i in range(rows)]
        q = Queue()
        time, fresh = 0, 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.put((r, c))
                    visited[r][c] = 1

        if  fresh == 0:
            return 0
            
        bfs()

        
        return time-1 if fresh == 0 else -1 # -1 to ignore the first  layer
