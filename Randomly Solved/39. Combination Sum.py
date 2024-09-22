class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def dfs(i, total, temp):
            if total == target:
                ans.append(temp.copy())
                return

            if i >= len(candidates) or total > target:
                return

            temp.append(candidates[i])
            total += candidates[i]
            dfs(i, total, temp)
            temp.pop()
            total -= candidates[i]
            dfs(i+1, total, temp)

        dfs(0, 0, [])
        return ans
