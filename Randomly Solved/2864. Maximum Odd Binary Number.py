class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        length = len(s)
        one_count = 0
        for c in s:
            if c == '1':
                one_count += 1

        ans = ""
        for i in range(one_count-1):
            ans += '1'
        for i in range(length - one_count):
            ans += '0'
        ans += '1'

        return ans
        
