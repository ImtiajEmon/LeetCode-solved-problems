class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        SUM = 0
        # prev_sum: count
        hash_tbl = {0: 1}
        sub_count = 0

        for num in nums:
            SUM += num
            temp = SUM - k
            sub_count += hash_tbl.get(temp, 0)
            hash_tbl[SUM] = hash_tbl.get(SUM, 0) + 1

        return sub_count
