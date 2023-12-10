class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n = len(matrix)
        m = len(matrix[0])
        t_mat = [[0 for j in range(n)] for i in range(m)]

        for i in range(m):
            for j in range(n):
                t_mat[i][j] = matrix[j][i]

        return t_mat
