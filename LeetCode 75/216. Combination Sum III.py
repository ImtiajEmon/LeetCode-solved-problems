class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []

        def dfs(i, total, temp):
            if total == n and len(temp) == k:
                ans.append(temp.copy())
                return

            if i > 9 or total > n or len(temp) > k:
                return

            # taking the i
            temp.append(i)
            dfs(i+1, total+i, temp)
            temp.pop()

            # not taking the i
            dfs(i+1, total, temp)

        dfs(1, 0, [])
        return ans
        
