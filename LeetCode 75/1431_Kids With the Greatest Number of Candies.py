class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans = []
        max_can = max(candies)

        for i in candies:
            if i + extraCandies >= max_can:
                ans.append(True)
            else:
                ans.append(False)
        return ans
