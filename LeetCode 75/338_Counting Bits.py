class Solution:
    def countBits(self, n: int) -> List[int]:
        def count_1_in(n):
            if n == 0:
                return 0
            cnt = 0
            for i in range(32):
                if (n & (1<<i)):
                    cnt += 1
            return cnt


        ans = []
        for i in range(n+1):
            ans.append(count_1_in(i))

        return ans
