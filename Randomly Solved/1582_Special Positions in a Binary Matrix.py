class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        def check(x, y):
            cnt1, cnt2 = 0, 0
            for i in mat[x]:
                if i == 1:
                    cnt1 += 1
            for i in range(len(mat)):
                if mat[i][y] == 1:
                    cnt2 += 1
            if cnt1 == 1 and cnt2 == 1:
                return True
            return False

        cnt = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    if check(i, j):
                        cnt += 1
        return cnt
