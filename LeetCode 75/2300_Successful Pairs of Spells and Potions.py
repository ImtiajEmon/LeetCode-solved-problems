class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        def count_pair(s):
            l = 0
            r = len(potions)-1
            partition_idx  = -1

            while l <= r:
                mid = (l+r) // 2
                if s * potions[mid] >= success:
                    partition_idx = mid
                    r = mid - 1
                else:
                    l = mid + 1

            if partition_idx == -1:
                return 0
            else:
                return len(potions) - partition_idx

        potions.sort()
        ans = []
        for s in spells:
            ans.append(count_pair(s))

        return ans
