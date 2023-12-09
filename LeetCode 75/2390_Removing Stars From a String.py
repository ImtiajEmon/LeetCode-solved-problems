class Solution:
    def removeStars(self, s: str) -> str:
        from collections import deque
        stack = deque()

        for  i in range(len(s)):
            if s[i] == '*':
                stack.pop()

            else:
                stack.append(s[i])

        ans = ''
        while stack:
            ans = stack.pop() +  ans

        return ans
