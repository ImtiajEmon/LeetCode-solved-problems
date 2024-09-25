class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []

        def dfs(i, total, temp):
            if total == target:
                ans.append(temp.copy())
                return
            
            if i >= len(candidates) or total > target:
                return

            temp.append(candidates[i])
            total += candidates[i]
            dfs(i+1, total, temp)
            temp.pop()
            total -= candidates[i]

            if i == len(candidates) - 1:
                return
            while(i < len(candidates)-1):
                if candidates[i] == candidates[i+1]:
                    i += 1
                else:
                    break
            dfs(i+1, total, temp)

        dfs(0, 0, [])
        return ans
