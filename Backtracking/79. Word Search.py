class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(x, y, n, m, i):
            if i == len(word):
                return True

            visited[x][y] = 1

            res = False
            # Up
            if x > 0 and not visited[x-1][y] and board[x-1][y] == word[i]:
                res = res or dfs(x-1, y, n, m, i+1)

            # Down
            if x < n-1 and not visited[x+1][y] and board[x+1][y] == word[i]:
                res = res or dfs(x+1, y, n, m, i+1)

            # Left
            if y > 0 and not visited[x][y-1] and board[x][y-1] == word[i]:
                res = res or dfs(x, y-1, n, m, i+1)

            # Right
            if y < m-1 and not visited[x][y+1] and board[x][y+1] == word[i]:
                res = res or dfs(x, y+1, n, m, i+1)

            # When I backtracked from a cell I made it unvisited.
            # Beacuse this cell maybe need to visit through another path in future
            visited[x][y] = 0

            return res


        n = len(board)
        m = len(board[0])

        visited = [[0 for i in range(m)] for j in range(n)]

        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    if dfs(i, j, n, m, 1):
                        return True
                    visited = [[0 for i in range(m)] for j in range(n)]

        return False
