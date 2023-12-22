class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        zero_cnt = [0]*n
        one_cnt = [0]*n

        temp = 0
        for i in range(n):
            if s[i] == '0':
                temp += 1
                zero_cnt[i] = temp
            

        temp = 0
        for i in range(n-1, -1,  -1):
            if s[i] == '1':
                temp += 1
                one_cnt[i] = temp

        ans = 0
        for i in range(1, n):
            ans = max(ans, zero_cnt[i-1]+one_cnt[i])
    
        return ans
