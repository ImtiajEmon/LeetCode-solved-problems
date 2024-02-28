class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        cnt = 0
        for i in range(0, 32):
            mask = (1 << i)
            if (c & mask):
                # ith bit of C is 1. That means to make the ith bit of (a OR b) 1
                # we need at least one 1 in ith bit either in a or b.
                # So, we need to flip one bit when both a and b's ith bit is 0
                if (a & mask) == 0 and (b & mask) == 0:
                    cnt += 1
            else:
                # To make it 0 we need both a and b's bit 0
                if (a & mask):
                    cnt += 1
                if (b & mask):
                    cnt += 1

        return cnt
