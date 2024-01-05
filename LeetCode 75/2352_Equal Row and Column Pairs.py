class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        def isequal(i, j, n):
            for x in range(n):
                if grid[i][x] != grid[x][j]:
                    return False
            return True
        
        n = len(grid)
        cnt = 0

        for i in range(n):
            for  j in range(n):
                if isequal(i, j, n):
                    cnt += 1

        return cnt

