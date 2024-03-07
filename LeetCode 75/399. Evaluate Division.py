class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)
        visited = set()

        def dfs(a, b):
            nonlocal prod
            visited.add(a)

            if a == b:
                ans.append(prod)
                return

            for pair in adj[a]:
                v, cost = pair
                if v not in visited:
                    prod *= cost
                    dfs(v, b)
                    prod /= cost



        for i, eq in enumerate(equations):
            u, v = eq
            cost = values[i]
            adj[u].append((v, cost))
            adj[v].append((u, 1/cost))

        ans = []
        prod = 1
        for qu in queries:
            a, b = qu
            if a not in adj or b not in adj:
                ans.append(-1)
            elif a == b:
                ans.append(1)
            else:
                prod = 1
                visited.clear()
                temp_len = len(ans)
                dfs(a, b)
                if temp_len == len(ans):
                    ans.append(-1)
    
        return ans
