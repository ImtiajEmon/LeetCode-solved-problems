class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math
        def calculate_hour(k):
            hour = 0
            for n in piles:
                hour += math.ceil(n / k)

            return hour

        l, r = 1, max(piles)
        ans = 0
        while l <= r:
            mid = (l + r) // 2
            hour = calculate_hour(mid)

            if hour > h:
                l = mid + 1
            
            if hour <= h:
                ans = mid
                r = mid - 1

        return ans
