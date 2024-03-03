class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack  = []
        ans = [0] * len(temperatures)

        for i in range(len(temperatures)):
            if len(stack) == 0 or temperatures[i] <= stack[-1][0]:
                stack.append((temperatures[i], i))
            else:
                while stack and temperatures[i] > stack[-1][0]:
                    pair = stack.pop()
                    temp, idx = pair[0], pair[1]
                    ans[idx] = i - idx
                stack.append((temperatures[i], i))


        return ans
        
